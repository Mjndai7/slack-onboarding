# Generated by Django 3.0.1 on 2020-06-06 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("sequences", "0001_initial"),
        ("to_do", "0001_initial"),
        ("resources", "0001_initial"),
        ("badges", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="pendingadmintask",
            name="assigned_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="externalmessage",
            name="send_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="condition",
            name="admin_tasks",
            field=models.ManyToManyField(to="sequences.PendingAdminTask"),
        ),
        migrations.AddField(
            model_name="condition",
            name="badges",
            field=models.ManyToManyField(to="badges.Badge"),
        ),
        migrations.AddField(
            model_name="condition",
            name="condition_to_do",
            field=models.ManyToManyField(
                related_name="condition_to_do", to="to_do.ToDo"
            ),
        ),
        migrations.AddField(
            model_name="condition",
            name="external_messages",
            field=models.ManyToManyField(to="sequences.ExternalMessage"),
        ),
        migrations.AddField(
            model_name="condition",
            name="resources",
            field=models.ManyToManyField(to="resources.Resource"),
        ),
        migrations.AddField(
            model_name="condition",
            name="sequence",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conditions",
                to="sequences.Sequence",
            ),
        ),
        migrations.AddField(
            model_name="condition",
            name="to_do",
            field=models.ManyToManyField(to="to_do.ToDo"),
        ),
    ]
