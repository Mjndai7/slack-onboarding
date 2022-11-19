# Generated by Django 3.2.16 on 2022-11-19 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("slack_bot", "0001_initial"),
        ("organization", "0028_auto_20221117_0029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="slack_birthday_wishes_channel",
            field=models.ForeignKey(
                help_text=(
                    "Leave blank to disable this. Timing is based on when this was "
                    "enabled."
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="slack_bot.slackchannel",
                verbose_name=(
                    "This is the channel where the bot will send birthday wishes in. "
                ),
            ),
        ),
    ]
