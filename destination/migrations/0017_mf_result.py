# Generated by Django 3.2.5 on 2022-02-25 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('destination', '0016_rename_rateinfo_places_rateinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mf_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destination.places')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
