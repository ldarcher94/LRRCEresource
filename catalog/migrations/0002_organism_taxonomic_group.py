# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organism',
            name='taxonomic_group',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
