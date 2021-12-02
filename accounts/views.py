from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
#from django.http import request

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            
            if User.objects.filter(username = username).exists():
                messages.schoolname(request, 'Username Taken')#print('Username taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.schoolname(request, 'Email already exists')#print('Email already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.schoolname(request, 'User Created')#print('User Created')
                return redirect('login')
        else:
            messages.schoolname(request, 'Password Not matching')#print('Password Not matching ...')
            return redirect('register')
            

        return redirect('/') #this redirects to the following page
        
    else:
        return render(request, 'register.html') # this is actually GET method

'''
I django we just need to create a model object to and we can push the data
directly into the database because of ORM in django

Also we do not have to create a data model in django to push the data
it is already their in the django framework we can simply use it by :-

from django.contrib.auth.model import user, auth
'''
'''
WORKING OF THIS FILE (According to me)

Actually First request that this page gets is 'GET' and since for the GET request the page returns register.html therefor the other page opens then 
the form in the page register.html gives the POST method so in views.py file we assign different values passed by the user to the database and then 
pass a message from this page to the webpage FOR EXAMPLE "Password not matching" or 'User Created' etc  
'''

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password) # This will return an object if the entered creds(username and password) are valid else user will be none
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.schoolname(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')