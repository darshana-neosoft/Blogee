from django.shortcuts import render
from django.template import loader, Context
from django.shortcuts import redirect

# Create your views here.
# from django.template import Context

from .models import Poster
from django.http import HttpResponse

def index(request):
    posts = Poster.objects.all()
    template = loader.get_template('index.html')
    context = {'posts': posts}
    return render(request, 'index.html', context)

def post(request):
    if request.method == "POST":
        author = request.POST.get("article", "")
        article = request.POST.get("author", "")
        post = Poster(author=author, article=article)
        post.save()
        posts = Poster.objects.all()
        context = {'posts': posts}
    else:
        context = {}
    
    template = loader.get_template('index.html')
    return render(request, 'index.html', context)
def new(request):
    template = loader.get_template('index.html')
    return render(request, 'new.html')