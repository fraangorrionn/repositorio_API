from django.urls import path

from  .api_views import *

urlpatterns = [
    path('ordenes',orden_list),
]