from django.db.models import Sum
from datetime import datetime, timedelta
import os
import requests
import xml.etree.ElementTree as ET
import json

from .models import Data


TRACK_POST = set()


def process_get_data(url):
    response = requests.get(url)

    if response.status_code != 200:
        return None

    content_type = response.headers.get('content-type')
    if content_type == 'text/xml':
        root = ET.fromstring(response.json())
        date = root.find('date').text
        value = float(root.find('data').text)
    elif content_type == 'application/json':
        data = json.loads(response.json())
        date = data['date']
        value = float(data['data'])
    elif content_type == 'text/plain':
        data = response.json().split(' ')
        date = datetime.utcfromtimestamp(float(data[0])).strftime('%Y-%m-%d %H:%M')
        value = float(data[1])
    else:
        return None

    date = format_date(date)
    new_entry = Data(date=date, value=value)
    new_entry.save()

    check_sum(date)
    return None


def check_sum(date):
    now = datetime.now()
    start_of_day = datetime(now.year, now.month, now.day)
    end_of_day = start_of_day + timedelta(days=1)

    if start_of_day not in TRACK_POST:
        sum_of_values = Data.objects.filter(date__range=(start_of_day, end_of_day)).aggregate(Sum('value'))

        if sum_of_values['value__sum'] > 1000:
            response = requests.post(os.getenv('POST_SERVICE_URL'), data={'date': date})
            if response.status_code == 201:
                if len(TRACK_POST) > 0:
                    TRACK_POST.pop()
                TRACK_POST.add(start_of_day)
            else:
                return 'Post request error'


def format_date(date_string):
    formats = ['%Y-%m-%d %H:%M', '%d-%m-%Y %H:%M']
    for fmt in formats:
        try:
            dt = datetime.strptime(date_string, fmt)
            if dt.second == 0:
                dt = dt.replace(second=datetime.now().second)
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            pass
    try:
        dt = datetime.fromtimestamp(int(date_string))
        if dt.second == 0:
            dt = dt.replace(second=datetime.now().second)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        pass
    raise ValueError(f"Unrecognized date format: {date_string}")
