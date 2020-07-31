from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import TransferCreateForm
from .models import AppTransfer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class UserTransferList(LoginRequiredMixin, generic.ListView):
    # TODO
    #raise NotImplementedError
    model = AppTransfer
    template_name = 'transfers/user_transfer_list.html'

    # For future reference: get_queryset() is used to run a specific query on the database.
    # Here, the query retrieves the transactions make by the currently active user.
    def get_queryset(self):
        try:
            # figure out how to get the currently active user
            app_user = AppTransfer.objects.filter(user=self.request.user)
        except User.DoesNotExist:
            raise Http404
        else:
            # return self.app_transfer_user.app_user.all()
            return self.app_user.app_user.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_user'] = self.app_user
        return context


# class TransferCreateView(LoginRequiredMixin, generic.CreateView):
#     # TODO
#     # don't need to handle login_url here. It is taken care of
#     # in the settings.py file
#     raise NotImplementedError
#
#
# class TransferDetailsView(LoginRequiredMixin, generic.DetailView):
#     # TODO
#     raise NotImplementedError
