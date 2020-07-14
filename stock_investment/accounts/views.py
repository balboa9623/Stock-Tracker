from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import UserRegistrationForm

# Create your views here.
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/signup.html'
