# Generated by Django 3.2.10 on 2022-02-09 00:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("preboarding", "0006_alter_preboarding_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="preboarding",
            name="content_json",
            field=models.JSONField(default=dict),
        ),
    ]
