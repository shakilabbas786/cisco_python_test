from django.conf.urls import patterns, url
from routers import views
urlpatterns = patterns('',
    url(r'^home/$', views.home, name='home'),
    url(r'^create_random_routers/$', views.create_routers, name='create_routers'),
    url(r'^delete_router/$', views.delete_router, name='delete_router'),
)
