# Generated by Django 2.2.20 on 2021-08-05 13:59

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
