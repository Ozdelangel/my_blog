from django.db import models
from django.contrib.auth import get_user_model

class Posts(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField(default='')
    post = models.TextField(default='')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
