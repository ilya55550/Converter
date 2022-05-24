import requests
from django.shortcuts import render
from django.views import View
from .forms import *


class CurrencyConverterView(View):
    @staticmethod
    def api_list_currency():
        url = "https://cdn.cur.su/api/cbr.json"
        r = requests.get(url)
        data = r.json()
        list_currency = sorted(list(data['rates'].keys()))
        return list_currency

    @staticmethod
    def api_convertible(value, transfer_from, transfer_to):
        url = "https://cdn.cur.su/api/cbr.json"
        r = requests.get(url)
        data = r.json()
        result_convertible = round(value * data['rates'][transfer_from] / data['rates'][transfer_to], 3)
        return result_convertible

    def get(self, request):
        list_currency = self.api_list_currency()
        form = CurrencyConverterForm(list_currency=list_currency)
        return render(request, 'CurrencyConverter/currency_converter.html', {'form': form})

    def post(self, request):
        list_currency = self.api_list_currency()
        bound_form = CurrencyConverterForm(request.POST, list_currency=list_currency)
        if bound_form.is_valid():
            value = bound_form.cleaned_data['value']
            transfer_from = bound_form.cleaned_data['transfer_from']
            transfer_to = bound_form.cleaned_data['transfer_to']
            result_convertible = self.api_convertible(value, transfer_from, transfer_to)
            context = {
                'result_convertible': result_convertible,
            }
            return render(request, 'CurrencyConverter/currency_converter.html', context=context | {'form': bound_form})
        return render(request, 'CurrencyConverter/currency_converter.html', {'form': bound_form})
