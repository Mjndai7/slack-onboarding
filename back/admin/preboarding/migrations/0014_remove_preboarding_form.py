# Generated by Django 3.2.12 on 2022-03-10 00:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("preboarding", "0013_auto_20220221_1338"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="preboarding",
            name="form",
        ),
    ]
