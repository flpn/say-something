from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/submit', views.submit, name='submit'),
]