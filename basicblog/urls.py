from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'basicblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', 
    'blog.views.view_post', 
    name='view_blog_post'),
	url(r'^blog/category/(?P<slug>[^\.]+).html', 
    'blog.views.view_category', 
    name='view_blog_category'),
    # url(r'^view_post', 'blog.views.view_post', name ='view_post'),
    url(r'^admin/', include(admin.site.urls)),
]
##