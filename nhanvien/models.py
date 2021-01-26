from django.db import models

class Nhanvien(models.Model):
    nvid = models.CharField(max_length=20)
    nvname = models.CharField(max_length=100)
    nvemail = models.EmailField()
    nvcontact = models.CharField(max_length=300)
    class Meta:
        db_table = "nhanvien"

    def __str__(self):
        return self.nvid