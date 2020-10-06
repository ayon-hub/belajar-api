from django.db import models

# Create your models here.
class Belajar(models.Model):
    nama = models.CharField(max_length=20)
    motto = models.TextField(max_length=20)

#bisa bikin model baru jika membutuhkan data lain untuk di tampilkan
#setelah membuat class baru, harus di migrate lagi