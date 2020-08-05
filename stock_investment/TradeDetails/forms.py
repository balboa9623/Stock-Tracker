from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'


class TradeDetailsForm(forms.ModelForm):
    class Meta:
        model = models.StockDetail
        fields = ['stock_name', 'num_stocks_bought', 'num_stocks_sold', 'starting_price', 'ending_price',
                  'time_zone', 'date_purchased', 'date_sold']
        widgets = {
            'date_purchased': DateInput(),
            'date_sold': DateInput(),
        }
        # widgets = {
        #     'date_purchased': DatePickerInput(options={
        #         'format': 'MM/DD/YYYY',
        #         'showTodayButton': True,
        #     }),
        #     'date_sold': DatePickerInput(options={
        #         'format': 'MM/DD/YYYY',
        #         'showTodayButton': True,
        #     })
        # }