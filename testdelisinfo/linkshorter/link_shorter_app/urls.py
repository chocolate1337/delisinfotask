from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from .views import LinkAPIView


urlpatterns = [
    re_path(r'^api_url/?$', LinkAPIView.as_view(), name='get_short_url'),
    re_path(r'^delete/(?P<pk>\d+)', LinkAPIView.as_view(), name='delete'),
]