# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-11 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(max_length=500)),
                ('pair_id', models.IntegerField(max_length=5000)),
            ],
        ),
    ]