from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    when = models.DateTimeField(auto_now=True)