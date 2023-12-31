# Generated by Django 3.2.8 on 2021-10-23 02:15

from django.db import migrations, models

from misc import fernet_fields


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0005_auto_20211023_0209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accesstoken",
            name="account_id",
            field=models.CharField(blank=True, default="", max_length=22300),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="app_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="base_url",
            field=models.CharField(blank=True, default="", max_length=22300),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="bot_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="bot_token",
            field=fernet_fields.EncryptedTextField(
                blank=True, default="", max_length=10000
            ),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="client_id",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="client_secret",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="name",
            field=models.CharField(blank=True, default="", max_length=22300),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="redirect_url",
            field=models.CharField(blank=True, default="", max_length=22300),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="refresh_token",
            field=fernet_fields.EncryptedTextField(
                blank=True, default="", max_length=10000
            ),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="signing_secret",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="token",
            field=fernet_fields.EncryptedTextField(
                blank=True, default="", max_length=10000
            ),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="verification_token",
            field=models.CharField(default="", max_length=100),
        ),
    ]
