from django.conf.urls import url

from . import views

app_name = 'frontend'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='auth_user'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout'),
]

