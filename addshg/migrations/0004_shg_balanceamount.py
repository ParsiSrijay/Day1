# Generated by Django 3.0.1 on 2020-07-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addshg', '0003_loan'),
    ]

    operations = [
        migrations.AddField(
            model_name='shg',
            name='BalanceAmount',
            field=models.IntegerField(default=0),
        ),
    ]
