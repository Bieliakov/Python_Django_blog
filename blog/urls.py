from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^(?P<post_slug>[-_\w]+)$', views.detail, name='detail'),
    # ex: /blog/category/{{category_slug}}
    url(r'^category/(?P<category_slug>[-_\w]+)$', views.category, name='category'), 
    # ex: /blog/tag/{{tag_slug}}
    url(r'^tag/(?P<tag_slug>[-_\w]+)$', views.tag, name = 'tag'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    
]