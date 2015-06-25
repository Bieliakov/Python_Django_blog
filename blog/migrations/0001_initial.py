# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Comment id')),
                ('body', models.TextField(verbose_name='Comment body')),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Post id')),
                ('post_title', models.CharField(max_length=255, verbose_name='Post title')),
                ('post_slug', models.SlugField(unique=True, max_length=100)),
                ('post_pub_date', models.DateTimeField(verbose_name='Date published', editable=False)),
                ('post_modified', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 8, 54, 27, 584126, tzinfo=utc))),
                ('post_publish', models.BooleanField(default=True)),
                ('post_body', models.TextField(verbose_name='Post body')),
                ('general_theme', models.CharField(max_length=2, default='Lf', choices=[('Lf', 'lf'), ('JS', 'JS'), ('Py', 'Py')])),
                ('post_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post_pub_date'],
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('slug', models.SlugField(max_length=200, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='com_to_post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
