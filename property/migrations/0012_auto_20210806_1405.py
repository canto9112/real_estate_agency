# Generated by Django 2.2.20 on 2021-08-06 11:05

from django.db import migrations


def fill_flats_into_owners(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    Flats = apps.get_model('property', 'Flat')
    for owner in Owners.objects.all():
        flats = list(Flats.objects.filter(owner=owner.owner))
        owner.flat.set(flats, clear=True)


def move_backward(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    for owner in Owners.objects.all():
        owner.flat.set([], clear=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20210805_1951'),
    ]

    operations = [
        migrations.RunPython(fill_flats_into_owners, move_backward)
    ]
