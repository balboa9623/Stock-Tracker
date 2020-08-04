from django.db import models
from django.core.exceptions import ValidationError
import datetime

# returns the user model that's currently active in this project.
from django.contrib.auth import get_user_model
from django.urls import reverse
from djmoney.models.fields import MoneyField

User = get_user_model()  # gets objects off of the current user section

# Using custom template tag.
from django import template

register = template.Library()


# Create your models here.

# Deposit to Bank class
#   -> User
#   -> Transfer amount


# Deposit to App class
#   -> User
#   -> Transfer amount
#   -> initiated date
#   -> fulfilled date


# Transferred to app (from bank to app)
class AppTransfer(models.Model):
    user = models.ForeignKey(User, related_name="app_user", on_delete=models.CASCADE)
    transfer_amount = MoneyField(max_digits=200, currency_choices=[('USD', '$ - USD')])  # , default_currency="USD")
    date_initiated = models.DateField(auto_now=False, blank=False)
    date_fulfilled = models.DateField(auto_now=False, blank=False)

    def __str__(self):
        return f"{self.user}  |  {self.transfer_amount}"

    def clean(self):
        now = datetime.datetime.now().date()
        if self.date_initiated > now and self.date_fulfilled > now:
            raise ValidationError("DATE ERROR: Date field(s) cannot be a date in the future.")

        if self.date_fulfilled < self.date_initiated:
            raise ValidationError("DATE ERROR: The date in 'date initiated' should be a date prior to date in 'date "
                                  "fulfilled.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('transfers:single', kwargs={
            'username': self.user.username,
            'pk': self.pk
        })

    class Meta:
        ordering = ["date_fulfilled"]


# TODO - IMPORTANT
"""
    Figure out why Users field in App_Transfer in "../admin" is
        not editable and it is a dropdown list with no values.
"""
