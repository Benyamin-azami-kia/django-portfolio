from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    body=models.TextField()
    slug=models.SlugField(max_length=150, unique_for_date='created', null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        return super().save(*args, **kwargs)