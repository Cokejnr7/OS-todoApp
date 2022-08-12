from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, TaskForm


# Create your views here.
def home(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'main.html', context)


def createTask(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/home.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'no user exist with such username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'Succesfully logged out')
    return redirect('login')


def registerUser(request):
    form = RegisterForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            registerForm = form.save(commit=False)
            registerForm.username = registerForm.username.lower()
            registerForm.save()
            return redirect('home')

        else:
            messages.error(request, 'something went wrong')

    return render(request, 'register.html', context)
