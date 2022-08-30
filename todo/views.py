from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, TaskForm
from datetime import datetime as dt


# Create your views here.
@login_required()
def home(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    incomplete = Task.objects.filter(complete=False)
    context = {'tasks': tasks, 'incomplete': incomplete}

    return render(request, 'todo/home.html', context)


@login_required()
def createTask(request):
    user = request.user
    name = "create"
    form = TaskForm()
    context = {'form': form, "name": name}
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            messages.success(request, "new task created")
            return redirect('home')
        messages.error(request, "unable to create task something went wrong")
    return render(request, 'todo/create-task.html', context)


@login_required()
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    context = {'task': task}
    return render(request, 'todo/task-detail.html', context)


@login_required()
def updateTask(request, pk):
    name = "update"
    user = request.user
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'form': form, 'name': name}
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            messages.success(request, f"task {task.title[0:20]} updated")
            return redirect('home')
        else:
            messages.error(request,
                           "unable to update task something went wrong")
    return render(request, 'todo/create-task.html', context)


@login_required()
def deleteTask(request, pk):
    user = request.user
    task = Task.objects.get(id=pk, user=user)
    context = {'task': task}
    if request.method == "POST":
        task.delete()
        # return redirect('home')
      
    return render(request, 'todo/delete-task.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
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
    messages.success(request, 'logged out succesfully')

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
            context['form'] = form
            messages.error(request, 'something went wrong')

    return render(request, 'register.html', context)
