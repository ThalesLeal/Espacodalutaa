# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-24 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181018_1249'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set([('cart_key', 'product')]),
        ),
    ]
