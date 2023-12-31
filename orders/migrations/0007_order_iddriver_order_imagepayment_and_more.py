# Generated by Django 4.2.1 on 2023-06-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_iddriver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='idDriver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='imagePayment',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='latitudeDestination',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='latitudeDriver',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='latitudeMyLocation',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='longitudeDestination',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='longitudeDriver',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='longitudeMyLocation',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='minutes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='modelCar',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='nameCustomer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='nameDestinations',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='nameDriver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='nameLocation',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='numberOfPassengers',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='numberingPlate',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='offers',
            field=models.ManyToManyField(blank=True, to='orders.offer'),
        ),
        migrations.AddField(
            model_name='order',
            name='phoneCustomer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phoneDriver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='profileCustomer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='profileDriver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='ratingDriver',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='typeCar',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='vehicleImage',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
