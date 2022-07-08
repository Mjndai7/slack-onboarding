# Generated by Django 3.2.10 on 2022-01-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("integrations", "0007_auto_20211108_2230"),
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
                    (4, "Asana"),
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
                    (4, "Asana"),
                ]
            ),
        ),
    ]
