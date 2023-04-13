from threading import Thread

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, models
from .forms import UsersForm, addUserForm, createDatabaseForm
from .connectors import postgreConnect, sqlServer
from .models import datasetDetails, tableNames
from django.contrib import messages
from uuid import uuid4
from .thread import task


def index(request):
    return render(request, 'index.html')


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


def datasetLoad(request):
    rows = datasetDetails.objects.all()
    if rows is not None:
        print(rows)
        return render(request, 'datasetTable.html', {'rows': rows})
    else:
        return render(request, 'datasetTable.html')


def createDB(request):
    if request.method == 'POST':
        form = createDatabaseForm(request.POST)
        if form.is_valid():
            databaseName = form.cleaned_data['databaseName']
            sourceType = form.cleaned_data['sourceType']
            # print(sourceType)
            database = form.cleaned_data['database']
            schemaName = form.cleaned_data['schemaName']
            hostName = form.cleaned_data['hostName']
            password = form.cleaned_data['password']
            user = form.cleaned_data['username']
            port = form.cleaned_data['port']

            databaseForm = datasetDetails()
            unique_id = str(uuid4())
            databaseForm.dbid = unique_id
            databaseForm.database = database
            databaseForm.datasetName = databaseName
            databaseForm.hostName = hostName
            databaseForm.password = password
            databaseForm.sourceType = sourceType
            databaseForm.schemaName = schemaName
            databaseForm.username = user
            databaseForm.port = port

            if sourceType == 'postgresql':
                conn = postgreConnect(hostName, database, user, password, port)
                if conn is not None:
                    print("connection established")
                    databaseForm.save()
                    thread = Thread(target=task, args=(unique_id, ))
                    thread.start()
                    print("added")
                    r = datasetDetails.objects.filter(dbid=unique_id).values
                    print("inside r", r)
                    return redirect('/dataset/')
                else:
                    print("no connection")
                    messages.warning(request, "Connection cannot be established please check again")
            elif sourceType == 'sqlserver':
                conn = sqlServer(hostName, user, password, database)
                if conn is not None:
                    print("added")
                    databaseForm.save()
                    return redirect('/dataset/')
                else:
                    print("not established")
                    messages.warning(request, "Connection cannot be established please check again")
            else:
                print("not postrges")

    else:
        form = createDatabaseForm()
    return render(request, 'db.html', {'form': form})


def profiling(request):
    return render(request, 'profiling.html')


def dummy(request, pk_test):
    id = pk_test
    return render(request, 'dummy.html', {'id': id})


def addprofile(request):
    return render()
