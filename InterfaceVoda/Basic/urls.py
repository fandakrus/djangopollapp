from django.urls import path

from .views import index, controls, trigger

urlpatterns = [
    path('', index, name='index'),
    path('controls/', controls, name='controls'),
    path('trigger', trigger, name='trigger')
]
