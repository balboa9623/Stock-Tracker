from django.contrib import admin
from transfers.models import AppTransfer # , BankTransfer

# Register your models here.
admin.site.register(AppTransfer)
# admin.site.register(BankTransfer)