from django.conf.urls import  include, url
from . import views

from django.conf import settings

urlpatterns = [
    url(r'^index/$',views.index, name = 'index'),
    url(r'^index_tweet/$',views.index_tweet, name = 'index_tweet'),
    url(r'^Information/$', views.api_data_Information, name = 'api_data_Information'),
    url(r'^Tweets/$', views.api_data_Tweets, name = 'Tweets'),
]
if settings.DEBUG is False:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATICFILES_DIRS}), 
    ]
