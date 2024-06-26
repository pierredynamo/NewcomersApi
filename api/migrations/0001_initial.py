# Generated by Django 5.0.4 on 2024-04-21 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientsTypes",
            fields=[
                (
                    "type",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Residency status",
                    ),
                ),
            ],
            options={
                "verbose_name": "Residency status",
                "verbose_name_plural": "Residency status",
            },
        ),
        migrations.CreateModel(
            name="Countries",
            fields=[
                (
                    "country",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Country",
                    ),
                ),
                ("contrycode", models.CharField(max_length=3)),
            ],
            options={
                "verbose_name": "Country",
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "service_name",
                    models.CharField(
                        max_length=150,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Purpose of the Appointment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Service",
                "verbose_name_plural": "Services",
            },
        ),
        migrations.CreateModel(
            name="Clients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70, verbose_name="Name")),
                (
                    "mname",
                    models.CharField(
                        blank=True, max_length=70, null=True, verbose_name="Middle name"
                    ),
                ),
                (
                    "fistname",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="First name"
                    ),
                ),
                ("dob", models.DateField(verbose_name="Date of birth")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=20, verbose_name="Phone number")),
                ("address", models.CharField(max_length=100, verbose_name="Address")),
                ("dol", models.DateField(verbose_name="Date of arrival")),
                (
                    "dRP",
                    models.DateField(blank=True, null=True, verbose_name="Date of PR"),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.clientstypes",
                        verbose_name="Residency status",
                    ),
                ),
                (
                    "countryb",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.countries",
                        verbose_name="Country of birth",
                    ),
                ),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.CreateModel(
            name="Appointments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datetime", models.DateTimeField(verbose_name="Time of Appointment")),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.clients",
                        verbose_name="Client Name",
                    ),
                ),
                (
                    "service_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.services",
                        verbose_name="Purpose of the Appointment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Appointment",
                "verbose_name_plural": "Appointments",
            },
        ),
    ]
