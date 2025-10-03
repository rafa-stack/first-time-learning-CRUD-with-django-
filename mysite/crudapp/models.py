from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    kategori = models.CharField(max_length=100)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

# Create your models here.
