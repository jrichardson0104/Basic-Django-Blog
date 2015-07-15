from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, render
from .models import Blog, Category
from django.template import Template, Context, loader 


# Create your views here.
def index(request):
    category = Category.objects.all()
   
    postcount = {}

    for category in category:
        count = Blog.objects.filter(category=category).count()
        postcount[category.title] = count
        
    print(postcount)
    context = {

		"categories": Category.objects.all(),
		"posts": Blog.objects.all()[:5],
        "postcount": postcount,
	}

    return render(request, "index.html", context)

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]})