from django.shortcuts import render
from .models import Blog

def home(request):
  blogs = Blog.objects # 모델로부터 객체 목록을 전달받을 수 있음 (쿼리셋) # 메소드
  return render(request, 'home.html', {'blogs':blogs})


# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소드