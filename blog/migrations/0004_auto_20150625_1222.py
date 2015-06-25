# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150625_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='general_theme',
            field=models.CharField(max_length=2, choices=[('Lf', 'lf'), ('JS', 'JS'), ('Py', 'Py')], default='JS'),
        ),
    ]
