from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

class Article_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj): 
        return obj.updated_on
