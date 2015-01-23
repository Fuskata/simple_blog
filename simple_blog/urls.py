from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import Posts, Login, Logout, AddPost
#from main.views import 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?', Login.as_view()),
    url(r'^$', Posts.as_view()),
    url(r'^logout/?', Logout.as_view()),
	url(r'^addpost/?', AddPost.as_view()),
)
