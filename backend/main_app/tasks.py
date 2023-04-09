import os
import time
from celery import shared_task
from .service import process_get_data


@shared_task
def process_call_all_services():
    urls = [
        os.getenv('RESOURCE_FIRST_URL'),
        os.getenv('RESOURCE_SECOND_URL'),
        os.getenv('RESOURCE_THIRD_URL'),
    ]

    for url in urls:
        process_get_data(url)

    time.sleep(5)

    return
