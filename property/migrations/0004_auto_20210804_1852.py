# Generated by Django 2.2.20 on 2021-08-04 15:03

from django.db import migrations


def create_new_building(apps, schema_editor):

    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(create_new_building)
    ]

