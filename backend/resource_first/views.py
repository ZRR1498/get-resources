from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import random
import xml.etree.ElementTree as ET


class ResourceView(APIView):
    """Handler for receiving data on request from a third-party service in xml format"""

    def get(self, request):
        try:
            value = random.uniform(80, 100)
            date = datetime.now().strftime("%d-%m-%Y %H:%M")
            xml_data = ET.Element('root')
            ET.SubElement(xml_data, 'date').text = date
            ET.SubElement(xml_data, 'data').text = str(value)
            xml_string = ET.tostring(xml_data, encoding='unicode', method='xml')
            return Response(xml_string, content_type='text/xml')
        except Exception as e:
            error_message = f'An error occurred while generating XML data: {str(e)}'
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
