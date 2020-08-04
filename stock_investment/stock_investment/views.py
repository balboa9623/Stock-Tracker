from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("loginHome"))
        return super().get(request, *args, **kwargs)


class LoginPage(TemplateView):
    template_name = "home.html"

