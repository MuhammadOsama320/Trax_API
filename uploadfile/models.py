from django.db import models


# Create your models here.
class Customer(models.Model):
    status_choice = (
        ('Shipment - Delivered', 'Shipment - Delivered'), ('Shipment - Pending', 'Shipment - Pending'), ('Shipment - Cancel', 'Shipment - Cancel'), ('Shipment - Complete', 'Shipment - Complete'),
        ('Shipment - Return', 'Shipment - Return')
    )
    pickup_address_id = models.IntegerField(null=True, blank=True)
    show_information_on_air_waybill = models.CharField(max_length=50, null=True, blank=True)
    consignee_city_name = models.CharField(max_length=100, null=True, blank=True)
    consignee_name = models.CharField(max_length=150, null=True, blank=True)
    consignee_address = models.CharField(max_length=225, null=True, blank=True)
    consignee_phone_number_1 = models.CharField(max_length=150, null=True, blank=True)
    consignee_phone_number_2 = models.CharField(max_length=150, null=True, blank=True)
    consignee_email_address = models.EmailField(max_length=150, null=True, blank=True)
    self_collection = models.CharField(max_length=50, null=True, blank=True)
    order_id = models.CharField(max_length=50, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    item_product_type_id = models.CharField(max_length=50, null=True, blank=True)
    item_description = models.CharField(max_length=225, null=True, blank=True)
    item_quantity = models.CharField(max_length=100, null=True, blank=True)
    item_insurance = models.CharField(max_length=50, null=True, blank=True)
    product_value = models.IntegerField(null=True, blank=True)
    special_instructions = models.CharField(max_length=225, null=True, blank=True)
    estimated_weight = models.IntegerField(null=True, blank=True)
    mode_of_shipment_id = models.CharField(max_length=150, null=True, blank=True)
    same_day_timing_id = models.CharField(max_length=150, null=True, blank=True)
    collection_amount = models.IntegerField(null=True, blank=True)
    mode_of_payment_id = models.IntegerField(null=True, blank=True)
    charges_mode_id = models.IntegerField(null=True, blank=True)
    pieces = models.IntegerField(null=True, blank=True)
    shipper_reference_number_1 = models.CharField(max_length=150, null=True, blank=True)
    shipper_reference_number_2 = models.CharField(max_length=150, null=True, blank=True)
    shipper_reference_number_3 = models.CharField(max_length=150, null=True, blank=True)
    shipper_reference_number_4 = models.CharField(max_length=150, null=True, blank=True)
    shipper_reference_number_5 = models.CharField(max_length=150, null=True, blank=True)
    status = models.CharField(max_length=200, choices=status_choice, null=True, blank=True)
    tracking_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.consignee_name}-{self.status}'
