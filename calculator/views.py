from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request,'home.html')
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('num1')
        password=request.POST.get('num2')
        if username != None and password != None:
            return redirect('calci')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')
    
      
def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        conform = request.POST.get('num3')
        if password != conform:
            return render(request,'register.html',{'result':'ERROR'})
        user=User.objects.create_user(username=username,password=password)
        return redirect('login')
    return render(request,'register.html')   
def calci(request):
    resu = None
    error = None
    if request.method == 'POST':
        a= int(request.POST.get('num1'))
        b=int(request.POST.get('num2'))
        o=request.POST.get('op').lower()
        if o == 'add':
            resu = a+b
        elif o == 'sub':
            resu = a-b
        elif o == 'mul':
            resu = a*b 
        else:
            resu = 'invalid' 
        return redirect('result',a=a,b=b,resu=resu)
    return render(request,'calci.html')
    
def result(request,a,b,resu):
    return render(request,'result.html',{'num1':a,'num2':b,'resu':resu})

