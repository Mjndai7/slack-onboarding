# Generated by Django 3.2.13 on 2022-05-17 00:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sequences", "0034_auto_20220504_2305"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="integrationconfig",
            name="additional_data",
        ),
    ]
