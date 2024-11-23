from django.shortcuts import render
from .models import Blog
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def main(request):
    blogs = Blog.objects.all()
    template = loader.get_template('main.html')
    context = {
        'blogs': blogs
    }
    return HttpResponse(template.render(context, request))