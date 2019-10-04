from .views import home
from django.urls import path


app_name = 'weather'

urlpatterns = [
    path('', home, name='home'),
]
