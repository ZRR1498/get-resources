from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import random
import json


class ResourceView(APIView):
    """Handler for receiving data on request from a third-party service in json format"""

    def get(self, request):
        try:
            value = random.uniform(80, 100)
            date = datetime.now().strftime("%Y-%m-%d %H:%M")
            json_data = json.dumps({"data": value, "date": date})
            return Response(json_data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
