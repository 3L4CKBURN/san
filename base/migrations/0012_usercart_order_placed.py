# Generated by Django 5.0.3 on 2024-04-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_orderdetails_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
    ]
