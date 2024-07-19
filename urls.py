from . import views
from django.urls import path

urlpatterns = [
    path('',views.submit_obituary, name='home')
]