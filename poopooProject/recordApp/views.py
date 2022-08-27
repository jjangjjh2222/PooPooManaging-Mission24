from django.shortcuts import render, redirect
from recordApp.models import Post


def record(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'home.html', {'posts':posts})

# html 파일 경로 수정

def get_time(request):
    new_post = Post()

    hour_data = int(request.GET.get('hour'))
    min_data = int(request.GET.get('min'))
    sec_data = int(request.GET.get('sec'))
    
    new_post.hour = hour_data
    new_post.minute = min_data
    new_post.sec = sec_data
    new_post.save()
    return redirect('home')

