# Generated by Django 4.1 on 2022-10-27 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ft', '0003_admin_ft_entry_payment_method_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_ft_entry',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='admin_ft_entry',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='admin_ft_entry',
            name='jumlah_pohon',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='admin_ft_entry',
            name='nominal_uang',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='admin_ft_entry',
            name='pesan',
            field=models.TextField(default='-'),
        ),
    ]
