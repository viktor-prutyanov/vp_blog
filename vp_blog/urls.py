from django.conf.urls import url, include
from django.contrib import admin
from blog_posts.views import health

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^health$', health),
    url(r'^posts/', include('blog_posts.urls', namespace='blog_posts')),
]
