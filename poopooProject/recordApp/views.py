from django.shortcuts import render, redirect
from recordApp.forms import PostForm
from recordApp.models import Post

def home(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'home.html', {'posts':posts})

# html 파일 경로 수정


def postcreate(request):
    if request.method == 'POST' or request.method == "FILES":# request method가 POST일 경우
        form = PostForm(request.POST, request.FILES)# 입력값 저장
        if form.is_valid():
            form.save()
            return redirect('home') 

    else: # request method가 GET일 경우
        form = PostForm()# form 입력 html 띄우기
    return render(request, 'post_form.html', {'form':form})

def get_time(request):

    print('테스트 입니다.')
    print(request.method)
    return render(request, 'post_form.html')