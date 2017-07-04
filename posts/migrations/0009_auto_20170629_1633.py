# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 22:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20170627_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Text',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='Publish_Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]