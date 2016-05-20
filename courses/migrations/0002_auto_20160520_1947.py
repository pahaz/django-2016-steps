# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 19:47
from __future__ import unicode_literals

import core.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lesson_images'),
        ),
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='step',
            name='meta',
            field=core.fields.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='courses.Lesson'),
        ),
        migrations.AlterField(
            model_name='step',
            name='type',
            field=models.IntegerField(choices=[(1, 'markdown'), (2, 'poll'), (3, 'code')], editable=False),
        ),
    ]
