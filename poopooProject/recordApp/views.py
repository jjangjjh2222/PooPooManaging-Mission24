from django.shortcuts import render, redirect
from .models import Post

def record(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

# html 파일 경로 수정
