from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *
from ..messageapp.models import *
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def index(request):
    return render(request, 'users/index.html')
#------------------------------------------------------------------------
def signin(request):
    return render(request, 'users/login.html')
#------------------------------------------------------------------------
def register(request):
    return render(request, 'users/register.html')
#------------------------------------------------------------------------
def dashboard(request):
    if 'userlevel' not in request.session:
        return redirect('/')
    context={
        'currentuser':User.objects.get(email=request.session['email']),
        'users':User.objects.all().values()
    }
    return render(request, 'users/dashboard.html',context)
#------------------------------------------------------------------------
def add(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = User.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
    
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/users/register')
    
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        request.session['email']=request.POST['email']
        user = User.objects.create()
        user.userlevel=0
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.email = request.POST['email']
        user.pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        request.session['userlevel']=user.userlevel
        messages.success(request, "User successfully added")
        # redirect to a success route
        return redirect('/dashboard')
#------------------------------------------------------------------------
def dashboardadmin(request):
    if 'userlevel' not in request.session:
        return redirect('/')
    if request.session['userlevel']!=9:
        return redirect('/')
    context={
        'users':User.objects.all().values()
    }
    return render(request, 'users/dashboardadmin.html', context)
#------------------------------------------------------------------------
def adminadd(request):
  
    # pass the post data to the method we wrote and save the response in a variable called errors
  
    errors = User.objects.basic_validator(request.POST)
       
        # check if the errors object has anything in it
   
    if len(errors):
        
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/users/new')

    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        user = User.objects.create()
        user.userlevel=0
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.email = request.POST['email']
        user.pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        messages.success(request, "User successfully added")
        
        # redirect to a success route
        return redirect('/dashboard/admin')
#------------------------------------------------------------------------
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/signin')
    request.session['email']=request.POST['email']
    user=User.objects.get(email=request.POST['email'])
    request.session['userlevel']=user.userlevel
    return redirect('/dashboard')
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def show(request, userid):
    if 'userlevel' not in request.session:
        return redirect('/')
    context={
        'user':User.objects.all().values().get(id=userid),
        'allmessages':Message.objects.all().filter(recipient=userid),
        'currentuser':User.objects.all().get(email=request.session['email']),
        'comments':Comment.objects.all()
    }
    return render(request, 'users/thewall.html', context)
#------------------------------------------------------------------------
def logout(request):
    del request.session['userlevel']
    return redirect('/')
#------------------------------------------------------------------------
def delete(request,userid):
    if request.session['userlevel'] != 9:
        return redirect('/')
    if 'userlevel' not in request.session:
        return redirect('/')
    user=User.objects.get(id=userid)
    user.delete()
    return redirect('/dashboard/admin')
#------------------------------------------------------------------------
def showedit(request,userid):
    if request.session['userlevel'] != 9:
        return redirect('/')
    if 'userlevel' not in request.session:
        return redirect('/')
    redirectstr='/users/'+str(userid)+'/edit'
    return redirect(redirectstr)
def edit(request,userid):
    if request.session['userlevel'] != 9:
        return redirect('/')
    if 'userlevel' not in request.session:
        return redirect('/')
    user=User.objects.get(id=userid)
    context={
        'user':user
    }
    return render(request, 'users/edit.html',context)
#------------------------------------------------------------------------
def update(request, userid):
    if request.session['userlevel'] != 9:
        return redirect('/')
    redirectstr='/users/'+str(userid)+'/edit'
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(redirectstr)

    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        user = User.objects.get(id=userid)
        user.userlevel=0
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.email = request.POST['email']
        user.pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        messages.success(request, "User successfully updated")
        return redirect('/dashboard/admin')
def useredit(request,userid):
    if 'userlevel' not in request.session:
        return redirect('/')
    user=User.objects.get(id=userid)
    context={
        'user':user
    }
    return render(request, 'users/useredit.html',context)
def userupdate(request, userid):
    if 'userlevel' not in request.session:
        return redirect('/')
    redirectstr='/users/edit/'+str(userid)
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(redirectstr)

    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        user = User.objects.get(id=userid)
        user.userlevel=0
        user.firstname = request.POST['firstname']
        user.lastname = request.POST['lastname']
        user.email = request.POST['email']
        request.session['email'] = request.POST['email']

        user.pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.save()
        messages.success(request, "User successfully updated")
        return redirect('/dashboard')
