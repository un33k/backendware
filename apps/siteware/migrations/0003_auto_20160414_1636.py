# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteware', '0002_auto_20160405_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentcode',
            options={'verbose_name': 'Comments'},
        ),
        migrations.AlterField(
            model_name='commentcode',
            name='code',
            field=models.TextField(blank=True, help_text='Third-party "Comment" Code. (e.g. Facebook, Disqus)', null=True, verbose_name='Comment Code'),
        ),
        migrations.AlterField(
            model_name='commentcode',
            name='name',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Disqus', 'Disqus')], default='Disqus', max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='commentcode',
            unique_together=set([('name',)]),
        ),
    ]
