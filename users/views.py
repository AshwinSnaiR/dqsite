from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, models
from .forms import UsersForm, addUserForm


def index(request):
    return render(request, 'login.html')


def user_login(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                print("successfull")
            else:
                print("not success")
            print(username, password)
    else:
        form = UsersForm()
    return render(request, 'login.html', {'form': form})


def create_User(request):
    if request.method == 'POST':
        form = addUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = models.User.objects.create_user(username, email, password)
            user.save()
    else:
        form = addUserForm()
    return render(request, 'addUser.html', {'form': form})

