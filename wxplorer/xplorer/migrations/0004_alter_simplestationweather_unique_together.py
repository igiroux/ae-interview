# Generated by Django 4.2.2 on 2023-07-07 09:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("xplorer", "0003_alter_simplestationweather_temperature"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="simplestationweather",
            unique_together={("forecast_time", "station")},
        ),
    ]
