from django.db import models
from django.db.models import permalink
from autoslug import AutoSlugField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')
    slug = AutoSlugField(populate_from='title')


    def __str__(self):
       return str(self.title)
       
    @permalink
    def get_absolute_url(self):
       return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='title')
    

    def __str__(self):
    	return str(self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

        ########