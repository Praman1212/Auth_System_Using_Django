from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request,'auth/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST.get('confirmpassword')

        myuser = User.objects.create_user(username,email, password)
        myuser.firstname = firstname
        myuser.lastname = lastname

        myuser.save()
        messages.success(request,"Your account have been successfully created.")

        return redirect('signin')


    return render(request,"auth/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        user = authenticate(username= username, password=password, confirmpassword=confirmpassword)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'auth/index.html', {'firstname': fname})

        else:
            messages.error(request, 'Bad Credentials ! ')
            return redirect('home')

    return render(request,"auth/signin.html")

def signout(request):
    pass