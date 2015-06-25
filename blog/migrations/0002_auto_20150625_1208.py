# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date published'),
        ),
    ]
