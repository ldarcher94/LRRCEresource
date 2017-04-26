# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_organism_taxonomic_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link_title',
            new_name='link_accession',
        ),
        migrations.AddField(
            model_name='gene',
            name='genscan_pred_seq',
            field=models.TextField(blank=True, db_column='Genscan Prediction'),
        ),
    ]
