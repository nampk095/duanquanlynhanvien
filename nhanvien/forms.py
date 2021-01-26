from django import forms
from nhanvien.models import Nhanvien
class NhanvienForm(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields = "__all__"