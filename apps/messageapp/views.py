from django.shortcuts import render, redirect
from ..users.models import *
from .models import *
from django.contrib import messages


def newmessage(request,recipientid):
        # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Message.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
    redirectstr='/'+str(request.POST['hidden'])+'/show'
    
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(redirectstr)
    
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the user to be updated, make the changes, and save
        content = request.POST['messagecontent']
        print(request.POST['hidden'])
        this_user=User.objects.get(id=request.POST['hidden'])
        this_recipient=User.objects.get(id=recipientid)
        Message.objects.create(content=content,user=this_user,recipient=this_recipient)
        messages.success(request, "Message successfully posted")
        # redirect to a success route
        return redirect(redirectstr)

def newcomment(request):

        # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Comment.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
    redirectstr='/'+str(request.POST['hidden2'])+'/show'
    
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(redirectstr)
    
    else:
        content = request.POST['commentcontent']
        print(request.POST['hidden'])
        this_message=Message.objects.get(id=request.POST['hidden'])
        this_user=User.objects.get(id=request.POST['hidden2'])
        Comment.objects.create(content=content,message=this_message,ucomment=this_user)
        return redirect(redirectstr)