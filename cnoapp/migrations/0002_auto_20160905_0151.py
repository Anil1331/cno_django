# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('image_url', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='referral',
            field=models.BooleanField(default=False),
        ),
    ]