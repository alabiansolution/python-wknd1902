# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-07-13 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=models.TextField(default='eiueuwhuywweueue'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
