from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def login(request):

    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']

        credentials = auth.authenticate(username=userName, password=password)
        if credentials is not None:
            auth.login(request, credentials)
            print("Successfully Logged in")
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        firstName = request.POST['first-name']
        lastName = request.POST['last-name']
        userName = request.POST['user-name']
        emaiId = request.POST['email']
        password = request.POST['password']
        passwordConf = request.POST['password-confirm']

        if password == passwordConf:
            if User.objects.filter(username=userName):
                messages.info(request, "Username already exists")
                print("Username already exists")
                return redirect('register')
            elif User.objects.filter(email=emaiId):
                messages.info(request, "Email Id already exists")
                print("Email Id already exists")
                return redirect('register')
            else:
                newUser = User.objects.create_user(username=userName, first_name=firstName, last_name=lastName, email=emaiId, password=password)
                newUser.save()
                messages.info(request, "User Registered successfully")
                print("User Registered successfully")
                return redirect('login')
        else:
            messages.info(request, "Passwords are not same")
            print("Passwords are not same")
            return redirect('register')
        return redirect('/')
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')