from rest_framework import generics

from .models import Data
from .serializers import DataSerializer


class DataListView(generics.ListCreateAPIView):
    """Handler for get data"""

    queryset = Data.objects.all()
    serializer_class = DataSerializer
