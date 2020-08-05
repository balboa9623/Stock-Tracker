# Generated by Django 3.0.3 on 2020-08-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('TradeDetails', '0002_auto_20200805_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_user', to='accounts.Users'),
        ),
    ]