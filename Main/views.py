from django.shortcuts import render
from .models import MainPage
def mainpagefun(request):
    items = MainPage.objects.all()
    sysplans = items.filter(SuperiorID=1)
    links = items.filter(SuperiorID=5)
    operations = items.filter(SuperiorID=2)
    return render(request,'MainPage.html',context={'sysplans':sysplans,'links':links,'operations':operations})