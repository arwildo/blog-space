from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from taggit.managers import TaggableManager


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    #content = models.TextField()
    content = HTMLField('Content')
    created_on = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/'+self.slug+'/'
