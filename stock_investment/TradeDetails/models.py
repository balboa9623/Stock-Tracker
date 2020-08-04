from django.db import models
from accounts.models import Users
from django.db.models.functions import Cast
import pytz
from djmoney.models.fields import MoneyField

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
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    stock_name = models.CharField(max_length=100, blank=False)
    num_stocks_bought = models.DecimalField(max_digits=100, decimal_places=4, blank=False)
    num_stocks_sold = models.DecimalField(max_digits=100, decimal_places=5, blank=False)

    starting_price = MoneyField(max_digits=20, decimal_places=5, default_currency="USD", blank=False)
    ending_price = MoneyField(max_digits=25, decimal_places=5, default_currency="USD", blank=False)
    net_profit = MoneyField(max_digits=100, decimal_places=5, default_currency="USD")

    TIMEZONES = extract_zone()
    time_zone = models.CharField(max_length=15, choices=TIMEZONES, default='US/Central')

    date_purchased = models.DateField(auto_now=False, blank=False)
    date_sold = models.DateField(auto_now=False, blank=False)

    def __str__(self):
        return f"{self.stock_name} - {self.user.username}"

    def save(self, *args, **kwargs):
        # save profit by subtracting ending_price - starting_price
        super(StockDetail, self).save(*args, **kwargs)
        profit_amt = StockDetail
        profit_amt.net_profit = (self.ending_price - self.starting_price) * Cast(self.num_stocks_sold)
        profit_amt.save()

    class Meta:
        ordering = ["date_purchased"]