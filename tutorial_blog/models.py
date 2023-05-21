from django.db import models

class Post(models.Model):
    #ブログのタイトル
    title = models.CharField(max_length=255)
    #記事の番号
    slug = models.SlugField()
    intro = models.TextField()
    #本文
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

