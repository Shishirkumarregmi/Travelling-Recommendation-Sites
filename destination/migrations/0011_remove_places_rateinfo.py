# Generated by Django 3.2.5 on 2022-02-15 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0010_auto_20220215_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='rateinfo',
        ),
    ]
