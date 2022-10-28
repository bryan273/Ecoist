# Generated by Django 4.1.2 on 2022-10-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participate', '0002_remove_participants_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='what_can_you_help_with',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='email_pendaftar',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='participants',
            name='nama_pendaftar',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='participants',
            name='phone_number',
            field=models.CharField(default='0', max_length=15),
        ),
    ]