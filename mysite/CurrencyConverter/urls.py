from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', CurrencyConverterView.as_view(), name='currency_converter'),

]
