# Generated by Django 5.0.6 on 2024-07-05 07:56

import datetime
import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reader", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NIC",
            fields=[
                (
                    "nic_numbber",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("delivery_date", models.DateField()),
                (
                    "expiration_date",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("delivery_date"),
                            "+",
                            models.Value(datetime.timedelta(days=1827)),
                        ),
                        output_field=models.DateField(),
                    ),
                ),
            ],
        ),
    ]
