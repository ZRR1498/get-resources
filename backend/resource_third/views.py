from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
import time


class ResourceView(APIView):
    """Handler for receiving data on request from a third-party service in string format"""

    def get(self, request):
        try:
            value = str(random.uniform(80, 100))
            date = str(float(time.time()))
            str_data = f'{date} {value}'
            return Response(str_data, content_type='text/plain')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
