# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artesania',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Artesano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=100)),
                ('num_dir', models.CharField(max_length=10)),
                ('clave_ref', models.IntegerField(verbose_name='Clave de referencia')),
                ('rfc', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=100)),
                ('num_dir', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedio', models.DateTimeField(verbose_name='Fecha de Registro')),
                ('fecha_entrega', models.DateTimeField(verbose_name='Fecha de Entrega')),
                ('artesania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artesanias.Artesania')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artesanias.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Telefono', models.CharField(max_length=100)),
                ('telefonos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artesanias.Artesano')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='pedidos',
            field=models.ManyToManyField(through='artesanias.Pedido', to='artesanias.Artesania'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artesania',
            name='artesano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artesanias.Artesano'),
        ),
    ]
