# Generated by Django 3.0.1 on 2020-06-06 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admin_tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="admintaskcomment",
            name="comment_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="admintask",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="admintask",
            name="new_hire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="new_hire_tasks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
