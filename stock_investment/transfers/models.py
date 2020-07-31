from django.db import models

# returns the user model that's currently active in this project.
from django.contrib.auth import get_user_model
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

# Transferred to bank (from app to bank)
# class BankTransfer(models.Model):
#     user = models.ForeignKey(User, related_name="bank_user", editable=False, on_delete=models.CASCADE)
#     transfer_amt = MoneyField(max_digits=200, decimal_places=2, default_currency="USD", blank=False)
#     date_fulfilled = models.DateField(auto_now=True, blank=False)
#
#     def __str__(self):
#         return f"$ {self.user}  |  {self.transfer_amt}"
#
#     class Meta:
#         ordering = ["date_fulfilled"]


# Transferred to app (from bank to app)
class AppTransfer(models.Model):
    user = models.ForeignKey(User, related_name="app_user", on_delete=models.CASCADE)
    # bank_transfer = models.ForeignKey(BankTransfer, on_delete=models.CASCADE, related_name="bank_transfer")
    transfer_amount = MoneyField(max_digits=200, currency_choices=[('USD', '$ - USD')])  # , default_currency="USD")
    date_initiated = models.DateField(auto_now=False, blank=False)
    date_fulfilled = models.DateField(auto_now=False, blank=False)

    def __str__(self):
        return f"{self.user}  |  {self.transfer_amount}"

    # def save(self, *args, **kwargs):
    #     super(AppTransfer, self).save(*args, **kwargs)
    #     bank_transfer = self.bank_transfer  # Creating an object based of on BankTransfer
    #     # copying data from AppTransfer model
    #     bank_transfer.transfer_amt = self.transfer_amount
    #     bank_transfer.date_fulfilled = self.date_fulfilled
    #     bank_transfer.save()


    class Meta:
        ordering = ["date_fulfilled"]


# TODO - IMPORTANT
"""
    Figure out why Users field in App_Transfer in "../admin" is
        not editable and it is a dropdown list with no values.
"""
