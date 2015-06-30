
# for resizing uploaded images
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# for converting strings with spaces into proper slugs
from django.template.defaultfilters import slugify 

'''
Instead of referring to User directly, you should reference the user model using django.contrib.auth.get_user_model(). This method will return the currently active User model – the custom User model if one is specified, or User otherwise.

When you define a foreign key or many-to-many relations to the User model, you should specify the custom model using the AUTH_USER_MODEL setting.
'''
from django.conf import settings

from django.db import models
from django.core.urlresolvers import reverse


import datetime
from django.utils import timezone

# import standard user model
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # delete website
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key = True)
    slug = models.SlugField(max_length=100, unique=True)
    '''
    name = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)
    '''
    def __str__(self):
            return self.name
    
    
    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50, primary_key = True)
    slug = models.SlugField(max_length=100, unique=True)
    #
    #def save(self, *args, **kwargs):
    #        self.slug = slugify(self.name)
    #        super(Tag, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
        
        
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    id = models.AutoField('Post id', primary_key=True)
    title = models.CharField('Post title', max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    pub_date = models.DateTimeField('Date published', auto_now_add = True)
    modified = models.DateTimeField('Date modified', auto_now = True)
    publish = models.BooleanField(default = True)
    body = models.TextField('Post body')
    comments_enabled = models.BooleanField(default = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    objects = EntryQuerySet.as_manager()
    image = models.ImageField(upload_to='static/images/')
    
    image_thumbnail_big = ImageSpecField(source='image',
                                  processors=[ResizeToFill(150, 150)],
                                  format='JPEG',
                                  options={'quality': 60})
                                  
    image_thumbnail_small = ImageSpecField(source='image',
                                  processors=[ResizeToFill(80, 80)],
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
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-pub_date']

'''
class Post_has_categories(models.Model):
    category_id =  models.ForeignKey(Category)
    post_id =  models.ForeignKey(Post)
'''
    
class Comment(models.Model):
    id = models.AutoField('Comment id', primary_key=True)
    body = models.TextField('Comment body')
    pub_date = models.DateTimeField('Date published', auto_now_add = True)
    modified = models.DateTimeField('Date modified', auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment_to_post = models.ForeignKey(Post)
    
    def __str__(self):
        return self.body
        
    class Meta:
        verbose_name = "Post comment"
        verbose_name_plural = "Post comments"
        ordering = ["-pub_date"]
