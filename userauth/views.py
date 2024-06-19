from django.shortcuts import render

def index1(request,):
    return render(request,'index1.html')
def loginn(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
