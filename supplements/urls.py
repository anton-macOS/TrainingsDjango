from django.urls import path
from .views import supplements
app_name = 'supplements'

urlpatterns = [
    path('', supplements, name='supplements')
]
