# Generated by Django 3.0.3 on 2020-07-31 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_amount_currency', djmoney.models.fields.CurrencyField(choices=[('USD', '$ - USD')], default='XYZ', editable=False, max_length=3)),
                ('transfer_amount', djmoney.models.fields.MoneyField(currency_choices=[('USD', '$ - USD')], decimal_places=2, max_digits=200)),
                ('date_initiated', models.DateField()),
                ('date_fulfilled', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_fulfilled'],
            },
        ),
    ]
