# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20170226_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='full_address',
            field=models.TextField(blank=True, verbose_name='Full address'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Full name'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='sub_districts',
            field=models.CharField(blank=True, max_length=255, verbose_name='Sub-districts'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='line4',
            field=models.CharField(blank=True, max_length=255, verbose_name='Fourth line of address'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='notes',
            field=models.TextField(blank=True, help_text='Tell us anything we should know when delivering your order.', verbose_name='Note'),
        ),
    ]
