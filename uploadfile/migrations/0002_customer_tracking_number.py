# Generated by Django 3.2.4 on 2021-06-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]