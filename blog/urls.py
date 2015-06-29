from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^(?P<post_slug>[-_\w]+)$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<post_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^category/(?P<category_slug>[-_\w]+)$', views.category, name='category'), 
    url(r'^tag/(?P<tag_slug>[-_\w]+)$', views.tag, name = 'tag'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    
]