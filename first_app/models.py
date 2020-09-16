from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=400)
    col1 = models.CharField(max_length=10, default=100)
    def __str__(self):
        return self.name