# Generated by Django 3.2.4 on 2021-06-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0004_alter_customer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Shipment - Delivered', 'Shipment - Delivered'), ('Shipment - Pending', 'Shipment - Pending'), ('Shipment - Cancel', 'Shipment - Cancel'), ('Shipment - Complete', 'Shipment - Complete'), ('Shipment - Return', 'Shipment - Return')], max_length=200),
        ),
    ]
