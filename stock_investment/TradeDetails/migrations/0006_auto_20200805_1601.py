# Generated by Django 3.0.3 on 2020-08-05 16:01

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('TradeDetails', '0005_auto_20200805_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetail',
            name='net_profit',
            field=djmoney.models.fields.MoneyField(decimal_places=3, default_currency='USD', editable=False, max_digits=100),
        ),
    ]
