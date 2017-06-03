from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^frontend/', include('frontend.urls',namespace="frontend")),
    url(r'^admin/', admin.site.urls),
]

