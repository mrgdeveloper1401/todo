# Generated by Django 5.0.6 on 2024-06-21 20:30

import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workspace",
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
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                (
                    "workspce_name",
                    models.CharField(max_length=50, verbose_name="title workspace"),
                ),
                ("workspace_description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "workspce_type",
                    models.CharField(
                        choices=[
                            ("ed", "education"),
                            ("bs", "business"),
                            ("eng", "engineer"),
                            ("pr", "personal"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "background_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="workspace_image",
                        to="images.images",
                    ),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        related_name="workspace_members", to="accounts.profileuser"
                    ),
                ),
            ],
            options={
                "verbose_name": "worspace",
                "verbose_name_plural": "workspaces",
                "db_table": "workspace",
            },
        ),
    ]
