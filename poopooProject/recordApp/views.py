from django.shortcuts import render, redirect
from recordApp.models import Post


def record(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

# html 파일 경로 수정



def get_time(request):

    hour_data = request.GET.get('hour')
    min_data = request.GET.get('min')
    sec_data = request.GET.get('sec')
    
    Post.hour 
    print(hour_data, min_data, sec_data)

