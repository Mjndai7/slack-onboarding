# Generated by Django 3.2.13 on 2022-05-05 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0014_organization_timed_triggers_last_check"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="custom_email_template",
            field=models.TextField(
                default="",
                help_text=(
                    "Leave blank to use the default one. "
                    "See documentation if you prefer your own."
                ),
                verbose_name="This is the default email template",
            ),
        ),
    ]
