from django.db import models

# Create your models here.
class Belajar(models.Model):
    nama = models.CharField(max_length=20)
    motto = models.TextField(max_length=20)