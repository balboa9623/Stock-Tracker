from django.contrib import admin
from transfers.models import BankTransfer, AppTransfer

# Register your models here.
admin.site.register(AppTransfer)
admin.site.register(BankTransfer)