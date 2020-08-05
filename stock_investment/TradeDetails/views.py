from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from .forms import TradeDetailsForm
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

from . import models


# Create your views here.
class AddTradeDetails(LoginRequiredMixin, generic.CreateView, SelectRelatedMixin):
    # fields = ('stock_name', 'num_stocks_bought', 'num_stocks_sold', 'starting_price', 'ending_price',
    #              'time_zone', 'date_purchased', 'date_sold')
    model = models.StockDetail
    template_name = 'TradeDetails/trade_create.html'
    form_class = TradeDetailsForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class SingleTradeDetails(LoginRequiredMixin, generic.DetailView):
    model = models.StockDetail
    select_related = ('stock_name', 'starting_price', 'ending_price', 'date_purchased', 'date_sold', 'net_profit')
    template_name = 'TradeDetails/trade_details.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))