from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    title=models.CharField(max_length=200,null=False)
    description=models.TextField(null=True)
    is_complete=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title