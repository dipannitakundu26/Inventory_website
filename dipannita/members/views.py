from django.shortcuts import redirect, render
from django .views import generic
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegisterUserForm
# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
        # Redirect to a success page.
          return redirect('index')
        else:
           messages.success(request, ("Invalid login, try again..."))
           return redirect('login')

    else:
        return render(request,'members/login.html',{})

def register_user(request):
    if request.method=="POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, ("Your account has been created successfully..."))
            return redirect('index')
        else:
            form=RegisterUserForm()
    
    return render(request,'members/register.html',{'form': RegisterUserForm})
    
def logout_user(request):
    logout(request)
    return redirect('index')

