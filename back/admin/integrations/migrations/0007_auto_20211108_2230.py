# Generated by Django 3.2.8 on 2021-11-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0006_auto_20211023_0215"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accesstoken",
            name="integration",
            field=models.IntegerField(
                choices=[
                    (0, "Slack bot"),
                    (1, "Slack account creation"),
                    (2, "Google account creation"),
                    (3, "Google Login"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="scheduledaccess",
            name="integration",
            field=models.IntegerField(
                choices=[
                    (0, "Slack bot"),
                    (1, "Slack account creation"),
                    (2, "Google account creation"),
                    (3, "Google Login"),
                ]
            ),
        ),
    ]
