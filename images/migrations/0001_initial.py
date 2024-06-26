# Generated by Django 5.0.6 on 2024-06-21 20:30

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Images",
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
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(
                        auto_now_add=True, verbose_name="create model"
                    ),
                ),
                (
                    "update_at",
                    django_jalali.db.models.jDateTimeField(
                        auto_now=True, verbose_name="update model"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field="image_height",
                        upload_to="images/%Y/%m/%d",
                        width_field="image_width",
                    ),
                ),
                ("image_hash", models.CharField(blank=True, max_length=40, null=True)),
                ("image_alt", models.CharField(blank=True, max_length=50, null=True)),
                ("image_width", models.PositiveIntegerField(blank=True, null=True)),
                ("image_height", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "image_size",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "image",
                "verbose_name_plural": "images",
                "db_table": "image",
            },
        ),
    ]
