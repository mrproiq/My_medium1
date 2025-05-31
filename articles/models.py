from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=250, blank=True)
    body = RichTextUploadingField()
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.name}"

