from django.urls import path
from . import views


urlpatterns = [
    path('get-data/', views.DataListView.as_view(), name='get-data'),
]
