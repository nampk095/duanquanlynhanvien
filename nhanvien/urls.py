from django.contrib import admin
from django.urls import path
from nhanvien import views

app_name = 'nhanvien'
urlpatterns = [
    path('',views.show),
    path('addnv', views.addnv),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]