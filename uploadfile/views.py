import datetime
import pandas as pd
from django.contrib.sites import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .form import CustomerForm
from uploadfile.models import Customer
from .trax_api import get_status
from django.core.paginator import Paginator


# Create your views here.


class UploadFileView(TemplateView):
    template_name = 'upload.html'

    def post(self, request, *args, **kwargs):
        file1 = request.FILES['upload']
        read_file = pd.read_csv(file1)
        for row in read_file.to_dict(orient='records'):
            Customer.objects.update_or_create(
                consignee_name=row.get("Consignee Name") if row.get("Consignee Name") != 'nan' else '',
                pickup_address_id=row.get("Pickup Address ID") if row.get("Pickup Address ID") != 'nan' else '',
                show_information_on_air_waybill=row.get("Show Information on Air Waybill") if str(row.get(
                    "Show Information on Air Waybill")) != 'nan' else '',
                consignee_city_name=row.get("Consignee City Name") if row.get("Consignee City Name") != 'nan' else '',
                consignee_address=row.get("Consignee Address") if row.get("Consignee Address") != 'nan' else '',
                consignee_phone_number_1=row.get("Consignee Phone Number 1 (03000000000)") if row.get(
                    "Consignee Phone Number 1 (03000000000)") != 'nan' else '',
                consignee_phone_number_2=row.get("Consignee Phone Number 2 (03000000000)") if str(
                    row.get("Consignee Phone Number 2 (03000000000)")) != 'nan' else '',
                consignee_email_address=row.get("Consignee Email Address") if str(
                    row.get("Consignee Email Address")) != 'nan' else '',
                self_collection=row.get("Self Collection") if row.get("Self Collection") != 'nan' else '',
                order_id=row.get("Order ID") if row.get("Order ID") != 'nan' else '',
                order_date=datetime.datetime.strptime(row.get("Order Date (YYYY-MM-DD)"), '%d/%m/%Y') if row.get(
                    "Order Date (YYYY-MM-DD)") != 'nan' else '',
                item_product_type_id=row.get("Item Product Type ID") if row.get(
                    "Item Product Type ID") != 'nan' else '',
                item_description=row.get("Item Description") if row.get("Item Description") != 'nan' else '',
                item_quantity=(row.get("Item  Quantity")) if str(row.get("Item Quantity")) != 'nan' else '',
                item_insurance=row.get("Item Insurance") if row.get("Item Insurance") != 'nan' else '',
                product_value=row.get("Product Value") if row.get("Product Value") != 'nan' else '',
                special_instructions=row.get("Special Instructions") if row.get(
                    "Special Instructions") != 'nan' else '',
                estimated_weight=row.get("Estimated Weight (kg)") if row.get("Estimated Weight (kg)") != 'nan' else '',
                mode_of_shipment_id=row.get("Mode of Shipment ID") if row.get("Mode of Shipment ID") != 'nan' else '',
                same_day_timing_id=row.get("Same Day Timing ID") if str(row.get("Same Day Timing ID")) != 'nan' else '',
                collection_amount=row.get("Collection Amount") if row.get("Collection Amount") != 'nan' else '',
                mode_of_payment_id=row.get("Mode of Payment ID") if row.get("Mode of Payment ID") != 'nan' else '',
                charges_mode_id=row.get("Charges Mode ID") if (row.get("Charges Mode ID")) != 'nan' else '',
                pieces=row.get("Pieces") if row.get("Pieces") != 'nan' else '',
                shipper_reference_number_1=row.get("Shipper Reference Number 1") if str(
                    row.get("Shipper Reference Number 1")) != 'nan' else '',
                shipper_reference_number_2=row.get("Shipper Reference Number 2") if str(
                    row.get("Shipper Reference Number 2")) != 'nan' else '',
                shipper_reference_number_3=row.get("Shipper Reference Number 3") != 'nan' if str(
                    row.get("Shipper Reference Number 3")) != 'nan' else '',
                shipper_reference_number_4=row.get("Shipper Reference Number 4") if str(
                    row.get("Shipper Reference Number 4")) != 'nan' else '',
                shipper_reference_number_5=row.get("Shipper Reference Number 5") if str(
                    row.get("Shipper Reference Number 5")) != 'nan' else '',
                status=get_status(int(row.get("Tracking Number"))) if (row.get("Tracking Number")) != 'nan' else '',
                tracking_number=row.get("Tracking Number") if (row.get("Tracking Number")) != 'nan' else '')

        return redirect(reverse('data'))


class DataView(TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        status = self.request.GET.get('status')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if start_date and end_date and status and status != 'Shipment - All':
            customers = Customer.objects.filter(order_date__gte=start_date, order_date__lte=end_date,
                                                status=status)
        elif start_date and end_date:
            customers = Customer.objects.filter(order_date__gte=start_date, order_date__lte=end_date)
        elif status and status != 'Shipment - All':
            customers = Customer.objects.filter(status=status)
        else:
            customers = Customer.objects.all()

        paginator = Paginator(customers, 10)
        page_number = self.request.GET.get('page')
        kwargs['customers'] = paginator.get_page(page_number)

        kwargs['start_date'] = start_date
        kwargs['end_date'] = end_date
        kwargs['status'] = status
        return kwargs


class CustomerEditView(TemplateView):
    template_name = "customer_form.html"

    def get(self, request, *args, **kwargs):

        customer_id = kwargs.get("id")
        customer = Customer.objects.get(id=customer_id)
        form = CustomerForm(instance=customer)
        return render(request, self.template_name, {"customer_form": form})

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(id=kwargs.get('id'))
        form = CustomerForm(instance=customer, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('data'))
        else:
            return render(request, self.template_name, {"customer_form": form})
