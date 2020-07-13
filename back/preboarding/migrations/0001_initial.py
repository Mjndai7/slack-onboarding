# Generated by Django 3.0.1 on 2020-06-06 20:14

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('misc', '0001_initial'),
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preboarding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10200), blank=True, size=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('template', models.BooleanField(default=True)),
                ('form', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('picture', models.FileField(null=True, upload_to='')),
                ('content', models.ManyToManyField(to='misc.Content')),
                ('to_do', models.ManyToManyField(to='to_do.ToDo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
