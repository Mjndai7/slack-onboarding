# Generated by Django 3.1.2 on 2020-11-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_auto_20201124_1621"),
    ]

    operations = [
        migrations.AddField(
            model_name="preboardinguser",
            name="order",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
