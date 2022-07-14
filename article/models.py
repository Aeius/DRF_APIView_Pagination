from django.db import models

# Create your models here.
class Article(models.Model):
    #글 작성자, 글 제목, 카테고리, 글 내용
    user = models.CharField("작성자", max_length=20)
    title = models.CharField("제목", max_length=50)
    content = models.TextField("글내용")
    def __str__(self):
        return self.title