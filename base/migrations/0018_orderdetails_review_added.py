# Generated by Django 5.0.3 on 2024-04-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_orderdetails_date_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='review_added',
            field=models.BooleanField(default=False),
        ),
    ]
