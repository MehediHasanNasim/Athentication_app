from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import ProfilePicture
# Create your views here.

#Import for Login and Signup
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import ProfilePictureForm, UserCreationForm

def home(request):
    diction = {}
    return render(request, 'authentication/index.html', context=diction)

def notfoundpage(request):
    diction = {}
    return render(request, 'authentication/notfound.html', context=diction)


def loginpage(request):

    if(request.user.is_authenticated):
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.info(request, 'Incorrect Username or Password')

        diction = {}
        return render(request, 'authentication/login.html', context=diction)




def registerpage(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        myform = UserCreationForm()
        if request.method == 'POST':
            myform = UserCreationForm(request.POST)
            if myform.is_valid():
                myform.save(commit=True)
                messages.success(request, 'Account Created')
                return redirect('loginpage')

        diction = {'myform':myform}
        return render(request, 'authentication/signup.html', context=diction)
    


@login_required(login_url='loginpage')
def profile(request):
    user = request.user
    diction = {'user':user}
    return render(request, 'authentication/profile.html', context=diction)


@login_required(login_url='loginpage')
def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='loginpage')
def delete_my_account(request):
    if request.method=="POST":
        userdata = request.user.id
        delete_id =  User.objects.get(id=userdata)
        delete_id.delete()
        logout(request)
        return redirect('home')