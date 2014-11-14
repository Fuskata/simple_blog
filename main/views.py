from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# from main.models import Post
# Create your views here.


class Posts(View):
    def get(self, request):
        return HttpResponse(render(request, 'posts.html', {}))