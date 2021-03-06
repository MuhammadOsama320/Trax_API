# Generated by Django 3.2.4 on 2021-06-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_address_id', models.IntegerField(blank=True, null=True)),
                ('show_information_on_air_waybill', models.CharField(blank=True, max_length=50, null=True)),
                ('consignee_city_name', models.CharField(blank=True, max_length=100, null=True)),
                ('consignee_name', models.CharField(blank=True, max_length=150, null=True)),
                ('consignee_address', models.CharField(blank=True, max_length=225, null=True)),
                ('consignee_phone_number_1', models.CharField(blank=True, max_length=150, null=True)),
                ('consignee_phone_number_2', models.CharField(blank=True, max_length=150, null=True)),
                ('consignee_email_address', models.EmailField(blank=True, max_length=150, null=True)),
                ('self_collection', models.CharField(blank=True, max_length=50, null=True)),
                ('order_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('item_product_type_id', models.CharField(blank=True, max_length=50, null=True)),
                ('item_description', models.CharField(blank=True, max_length=225, null=True)),
                ('item_quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('item_insurance', models.CharField(blank=True, max_length=50, null=True)),
                ('product_value', models.IntegerField(blank=True, null=True)),
                ('special_instructions', models.CharField(blank=True, max_length=225, null=True)),
                ('estimated_weight', models.IntegerField(blank=True, null=True)),
                ('mode_of_shipment_id', models.CharField(blank=True, max_length=150, null=True)),
                ('same_day_timing_id', models.CharField(blank=True, max_length=150, null=True)),
                ('collection_amount', models.IntegerField(blank=True, null=True)),
                ('mode_of_payment_id', models.IntegerField(blank=True, null=True)),
                ('charges_mode_id', models.IntegerField(blank=True, null=True)),
                ('pieces', models.IntegerField(blank=True, null=True)),
                ('shipper_reference_number_1', models.CharField(blank=True, max_length=150, null=True)),
                ('shipper_reference_number_2', models.CharField(blank=True, max_length=150, null=True)),
                ('shipper_reference_number_3', models.CharField(blank=True, max_length=150, null=True)),
                ('shipper_reference_number_4', models.CharField(blank=True, max_length=150, null=True)),
                ('shipper_reference_number_5', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Complete', 'Complete'), ('Return', 'Return')], max_length=200)),
            ],
        ),
    ]
