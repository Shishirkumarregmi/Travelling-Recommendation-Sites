# Generated by Django 3.2.5 on 2022-02-15 13:19

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_remove_profile_register_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='defaultpp.jpg', upload_to=registration.models.content_file_name),
        ),
    ]
