# Generated by Django 3.2.5 on 2022-03-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratinghome', '0008_auto_20220216_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateinfo',
            name='genres',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
