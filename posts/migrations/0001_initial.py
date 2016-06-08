# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height', null=True, upload_to=b'', width_field='width')),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]
