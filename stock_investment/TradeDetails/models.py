from django.db import models
from django.urls import reverse

from accounts.models import Users
from django.db.models.functions import Cast
import pytz
from djmoney.models.fields import MoneyField

from django.contrib.auth import get_user_model
User = get_user_model()  # gets objects off of the current user section

# Create your models here.

# user, stock name, # of stocks bought, starting price, ending price,
# date purchased, time purchased,
# date sold, time sold,
# time zone, profit/ loss


def extract_zone():
    time_zone = pytz.common_timezones
    US = []
    for zone in time_zone:
        if "US" in zone:
            # print(zone)
            US.append(zone)

    us_zones = tuple(zip(US,US))
    return us_zones


class StockDetail(models.Model):
    user = models.ForeignKey(User, related_name="stock_user", on_delete=models.CASCADE)

    stock_name = models.CharField(max_length=100, blank=False)
    num_stocks_bought = models.DecimalField(max_digits=100, decimal_places=4, blank=False)
    num_stocks_sold = models.DecimalField(max_digits=100, decimal_places=5, blank=False)

    starting_price = MoneyField(max_digits=20, decimal_places=3, default_currency="USD", blank=False)
    ending_price = MoneyField(max_digits=25, decimal_places=3, default_currency="USD", blank=False)
    net_profit = MoneyField(max_digits=100, decimal_places=3, default_currency="USD", editable=False)

    TIMEZONES = extract_zone()
    time_zone = models.CharField(max_length=15, choices=TIMEZONES, default='US/Central')

    date_purchased = models.DateField(auto_now=False, blank=False)
    date_sold = models.DateField(auto_now=False, blank=False)

    def __str__(self):
        return f"{self.user.username}  |  {self.stock_name}  |  {self.date_sold}"

    def save(self, *args, **kwargs):
        # save profit by subtracting ending_price - starting_price
        self.stock_name = self.stock_name.upper()
        sold = self.num_stocks_sold
        self.net_profit = (self.ending_price - self.starting_price) * sold
        # print(self.net_profit)
        # print(self.stock_name)
        super(StockDetail, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('TradeDetail:single', kwargs={
            'username': self.user.username,
            'pk': self.pk})

    class Meta:
        ordering = ["date_purchased"]
        unique_together = (('stock_name', 'date_purchased'), ('stock_name', 'date_sold'))
