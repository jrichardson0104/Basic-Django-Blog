from django.contrib import admin


# Register your models here.
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
	list_display = ["__str__", "category", "slug", "posted"]
	# class Meta: 
	# 	model = Blog
class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__str__"]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
