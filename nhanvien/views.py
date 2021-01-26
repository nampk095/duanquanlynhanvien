from django.shortcuts import render, redirect
from nhanvien.forms import NhanvienForm
from nhanvien.models import Nhanvien

# Create your views here.
def addnv(request):
    #nếu có gửi POST thì chạy
    if request.method == "POST":
        form = NhanvienForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = NhanvienForm()
    #Load giao diện
    return render(request,'index.html',{'form':form})
def show(request):
    tatcanhanvien = Nhanvien.objects.all()
    return render(request,"show.html",{'tatcanhanvien':tatcanhanvien})
def edit(request, id):
    nhanvien = Nhanvien.objects.get(id=id)
    return render(request,'edit.html', {'nhanvien':nhanvien})
def update(request, id):
    nhanvien = Nhanvien.objects.get(id=id)
    form = NhanvienForm(request.POST, instance=nhanvien)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'nhanvien': nhanvien})
def destroy(request, id):
    nhanvien = Nhanvien.objects.get(id=id)
    nhanvien.delete()
    return redirect("/show")