# Generated by Django 4.2.1 on 2023-06-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_is_active_chauffeurcall_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='imagePayment',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]