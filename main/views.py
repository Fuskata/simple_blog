from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Post
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class AddPost(View):
    def get(self, request):
        if request.user.is_authenticated():
       # posts = Post.objects.all()
            return HttpResponse(render(request, 'edit_post.html', {}))
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        header = request.POST['header']
        content = request.POST['content']
        publish = 'publish' in request.POST
        Post.objects.create(header=header, text=content)
        return HttpResponseRedirect('/')

class Posts(View):
    def get(self, request):
        posts = Post.objects.all()
        return HttpResponse(render(request, 'posts.html', {'posts': posts}))

class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
        	login(request, user)
        	return HttpResponseRedirect('/') 
        else:
        	return HttpResponse('Epic fail.')

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponse('<div style="text-align: center">Su~ccess. <i><a href="http://127.0.0.1:8000/">Go back?</a><br><br><a href="http://hdwallpaperfun.com/wp-content/uploads/2014/08/Free-Pictures-Of-Cats-Wallpaper-HD.jpg">Or some cat?</a></div></i>')
