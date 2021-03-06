"""blogSpace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import settings
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import Article_Sitemap

sitemaps = {
    'article': Article_Sitemap(),
}

if settings.ADMIN_ENABLED:
    urlpatterns = [
        path('admin/', admin.site.urls), 
        path('', include('blog.urls')),
    ]
else:
    urlpatterns = [
        path('', include('blog.urls')),
    ]
    

urlpatterns += [
    url(r'^robots\.txt$', TemplateView.as_view(template_name="blogSpace/robots.txt", content_type='text/plain')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
