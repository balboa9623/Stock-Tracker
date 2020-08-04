from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import TransferCreateForm
from .models import AppTransfer
from django import forms
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
class AllTransactionList(LoginRequiredMixin, generic.ListView):
    model = AppTransfer
    template_name = 'transfers/user_transfer_list.html'
    # For future reference: get_queryset() is used to run a specific query on the database.
    # Here, the query retrieves the transactions make by the currently active user.
    def get_queryset(self):
        try:
            self.app_user = User.objects.prefetch_related('app_user').get(username__iexact=self.kwargs.get('username'))
        except:
            raise Http404
        else:return self.app_user.app_user.all()

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['app_user'] = self.app_user
            return context


class CreateNewTransfer(LoginRequiredMixin, generic.CreateView, SelectRelatedMixin):
    # don't need to handle login_url here. It is taken care of
    # in the settings.py file
    fields = ('transfer_amount', 'date_initiated', 'date_fulfilled')

    model = AppTransfer
    template_name = "transfers/transfer_create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class TransferDetails(LoginRequiredMixin, generic.DetailView):
    model = AppTransfer
    select_related = ('transfer_amount', 'date_initiated', 'date_fulfilled')
    template_name = 'transfers/transfer_details.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
