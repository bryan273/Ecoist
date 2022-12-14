# Generated by Django 4.1 on 2022-10-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ft', '0002_admin_ft_entry_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_ft_entry',
            name='payment_method',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='admin_ft_entry',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
