from django.conf.urls import url, include
from django.contrib import admin
from vp_blog.views import health, index

urlpatterns = [
    url(r'^$', index),
    url(r'^index.html$', index),
    url(r'^health$', health),
    url(r'^posts/', include('blog_posts.urls', namespace='blog_posts')),
]
