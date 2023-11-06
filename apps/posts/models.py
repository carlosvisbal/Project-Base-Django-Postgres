from django.db import models

# Create your models here.
class BaseModelos(models.Model):
  created = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  activo  = models.BooleanField(default=True)
  
  class Meta:
    abstract = True
    default_permissions = []

class Post(BaseModelos):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.CharField(max_length=255)
    