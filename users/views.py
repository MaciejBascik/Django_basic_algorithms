from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def loginView(request):
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is None:
                    context = {"error":"Incorrect username or password! Try again!"}
                    return render(request, "users/login.html", context)
                if user:
                    login(request, user)
                    context = {"success":"You are logged in!","username":username}
                    return render(request, "main/home.html", context)
            return render(request, "users/login.html", {})

def registerView(request):
            if request.method == "POST":
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')

                if User.objects.filter(username = username).first():
                    return render(request, "users/register.html", {"error":"This username is already taken!"})
                elif User.objects.filter(email = email).first():  
                    return render(request, "users/register.html", {"error":"This email is already taken!"})
                user = User.objects.create_user(username, email, password)
                user.save()
                return render(request, "main/home.html", {"success":"you have created account!"})
            return render(request, "users/register.html", {})

def logoutView(request):
    logout(request)  
    return render(request, "main/home.html", {"successLogOut":"You have just logout!"})
