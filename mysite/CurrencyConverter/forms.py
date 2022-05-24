from django import forms


class CurrencyConverterForm(forms.Form):
    value = forms.IntegerField(label='Количество')

    def __init__(self, *args, list_currency, **kwargs):
        super(CurrencyConverterForm, self).__init__(*args, **kwargs)
        choices = tuple((i, i) for i in list_currency)
        self.fields['transfer_from'] = forms.ChoiceField(label='из', choices=choices)
        self.fields['transfer_to'] = forms.ChoiceField(label='в', choices=choices)
