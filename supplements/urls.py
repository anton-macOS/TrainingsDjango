from django.urls import path
from .views import supplements

urlpatterns = [
    path('', supplements, name='supplements')
]
