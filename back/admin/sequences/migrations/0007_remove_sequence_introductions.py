# Generated by Django 3.1.2 on 2020-11-25 01:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sequences", "0006_condition_introductions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sequence",
            name="introductions",
        ),
    ]
