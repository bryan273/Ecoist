# Generated by Django 4.1 on 2022-10-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_ft_entry',
            name='username',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
