# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class MainPage(models.Model):
    ItemName = models.CharField(max_length=20,verbose_name="名称")
    SuperiorID = models.IntegerField(verbose_name="上级项ID")
    SuperiorName = models.CharField(max_length=20,verbose_name="上级项名称")
    LinkPage = models.CharField(max_length=100,verbose_name="链接地址")