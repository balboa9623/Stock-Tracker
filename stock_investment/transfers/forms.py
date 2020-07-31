from django.contrib.auth import get_user_model  # returns currently active user model
from django import forms
from .models import AppTransfer


class TransferCreateForm(forms.ModelForm):
    raise NotImplementedError

