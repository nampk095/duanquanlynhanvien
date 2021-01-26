from django.contrib import admin
#import thêm vào
from .models import Nhanvien

# Register your models here.
#Đăng ký model Nhanvien vào admin panel
admin.site.register(Nhanvien)