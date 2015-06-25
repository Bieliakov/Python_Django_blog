# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150625_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Post comments', 'verbose_name': 'Post comment', 'ordering': ['-comment_pub_date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='comment_author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='id',
            new_name='comment_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='com_to_post',
            new_name='comment_to_post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 6, 25, 10, 9, 35, 706604, tzinfo=utc), verbose_name='Date modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 25, 10, 13, 22, 281563, tzinfo=utc), verbose_name='Date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_comments_enabled',
            field=models.BooleanField(default=True),
        ),
    ]
