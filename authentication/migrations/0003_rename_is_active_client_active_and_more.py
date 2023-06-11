# Generated by Django 4.2.1 on 2023-06-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_client_id_alter_driver_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='is_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='is_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='numbering_plate',
            new_name='numberingPlate',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='personal_address',
            new_name='personalAddress',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='is_subscribe',
            new_name='subscribe',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='vehicle_image',
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicleImage',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='driver',
            name='date',
            field=models.CharField(max_length=255),
        ),
    ]