from django.urls import path
from . import views


urlpatterns = [
    path('resource/', views.ResourceView.as_view(), name='get-data'),
]
