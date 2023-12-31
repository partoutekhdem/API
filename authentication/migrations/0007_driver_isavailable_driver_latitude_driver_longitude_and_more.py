# Generated by Django 4.2.1 on 2023-06-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_driver_subscribepath"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="available",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="driver",
            name="latitude",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="driver",
            name="longitude",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="driver",
            name="subscribePath",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="driver",
            name="subscribeDate",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
         migrations.RemoveField(
            model_name="driver",
            name="pathSubscribe",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
