# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artesanias', '0002_artesania_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefono',
            old_name='Telefono',
            new_name='telefono',
        ),
    ]
