from django.shortcuts import render
from recordApp.models import Post

# Create your views here.
def home(req):
    posts = Post.objects.filter().order_by('-date')
    return render(req, 'home.html', {'posts':posts})

