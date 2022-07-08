# Generated by Django 3.2.10 on 2022-02-09 00:44

from django.db import migrations

from misc.migration_scripts.content_migrations import (
    RunPythonWithArguments,
    migrate_wysiwyg_field,
)


class Migration(migrations.Migration):

    dependencies = [
        ("preboarding", "0007_preboarding_content_json"),
    ]

    operations = [
        RunPythonWithArguments(
            migrate_wysiwyg_field,
            context={"app": "preboarding", "model": "preboarding"},
        ),
    ]
