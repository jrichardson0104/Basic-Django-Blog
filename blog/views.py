from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, render
from .models import Blog, Category
from django.template import Template, Context, loader 

categories = Category.objects.all()
blogs = Blog.objects.all()
# Create your views here.
def index(request):
    
   
    # postcount = {}

    # for category in category:
    #     count = Blog.objects.filter(category=category).count()
    #     postcount[category.title] = count
        
    context = {

		"categories": categories,
		"posts": blogs,
	}

    return render(request, "index.html", context)

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug), 'categories':categories,})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5],'categories':categories,})