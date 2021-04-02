from django.conf.urls import url
from events import views

urlpatterns=[
    url(r'^$', views.PostListView.as_view(), name='event_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='event_new'), 
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='event_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='event_remove'),
   
]   