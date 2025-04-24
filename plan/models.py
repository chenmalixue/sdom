from django.db import models

# Create your models here.
class clsnetwork(models.Model):
    ItemName = models.CharField(max_length=20,verbose_name="名称")
