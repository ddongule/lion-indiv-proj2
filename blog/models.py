from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()

  # 어드민 사이트에 내가 쓴 글의 제목이 나타나게 하게 하기 위함
  def __str__(self):
    return self.title
  # model.~Field(추가데이터) 이런 느낌