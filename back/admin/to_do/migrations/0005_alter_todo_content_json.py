# Generated by Django 3.2.8 on 2021-11-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("to_do", "0004_todo_content_json"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="content_json",
            field=models.JSONField(default=dict),
        ),
    ]
