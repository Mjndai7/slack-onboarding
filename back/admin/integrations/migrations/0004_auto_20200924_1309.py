# Generated by Django 3.0.7 on 2020-09-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0003_auto_20200620_1938"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scheduledaccess",
            name="status",
            field=models.IntegerField(
                choices=[(0, "pending"), (1, "completed"), (2, "waiting on user")],
                default=0,
            ),
        ),
    ]
