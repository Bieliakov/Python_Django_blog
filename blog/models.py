from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.db import models
from django.core.urlresolvers import reverse

import datetime
from django.utils import timezone

from django.contrib.auth.models import User

class Tag(models.Model):
    slug = models.SlugField(max_length=200,primary_key=True)

    def __str__(self):
        return self.slug

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    post_id = models.AutoField('Post id', primary_key=True)
    post_title = models.CharField('Post title', max_length=255)
    post_slug = models.SlugField(max_length=100, unique=True)
    post_pub_date = models.DateTimeField('Date published', auto_now_add = True)
    post_modified = models.DateTimeField('Date modified', auto_now = True)
    post_publish = models.BooleanField(default = True)
    post_body = models.TextField('Post body')
    post_comments_enabled = models.BooleanField(default = True)
    post_author = models.ForeignKey(User)
    objects = EntryQuerySet.as_manager()
    post_tags = models.ManyToManyField(Tag)
    post_image = models.ImageField(upload_to='images/')
    post_thumbnail = ImageSpecField(source='post_image',
                                  processors=[ResizeToFill(100, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    
    life = 'Lf'
    python = 'Py'
    javascript = 'JS'
    topic_choices = (
        (life, 'lf'),
        (javascript, 'JS'),
        (python, 'Py'),
    )
    general_theme = models.CharField(max_length=2, choices = topic_choices, default = javascript)

    def __str__(self):
        return self.post_title
    
    def was_published_recently(self):
        return self.post_pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'post_pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-post_pub_date']



class Comment(models.Model):
    comment_id = models.AutoField('Comment id', primary_key=True)
    comment_body = models.TextField('Comment body')
    comment_pub_date = models.DateTimeField('Date published', auto_now_add = True)
    comment_modified = models.DateTimeField('Date modified', auto_now = True)
    comment_author = models.ForeignKey(User)
    comment_to_post = models.ForeignKey(Post)
    
    def __str__(self):
        return self.comment_body
        
    class Meta:
        verbose_name = "Post comment"
        verbose_name_plural = "Post comments"
        ordering = ["-comment_pub_date"]
