# Generated by Django 3.2.5 on 2022-02-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0013_auto_20220215_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
