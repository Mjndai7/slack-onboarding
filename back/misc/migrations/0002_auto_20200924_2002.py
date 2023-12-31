# Generated by Django 3.0.7 on 2020-09-24 20:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("misc", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="answer",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="content",
            name="content",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="content",
            name="items",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=list, verbose_name=models.TextField(blank=True)
            ),
        ),
    ]
