# Generated by Django 3.2.6 on 2021-08-14 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iranian_cities', '0002_rename_shhahr_dehestan_shahr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dehestan',
            name='shahr',
        ),
    ]