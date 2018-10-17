from django.shortcuts import render, redirect
from ..users.models import *
from .models import *
from django.contrib import messages


def newmessage(request,recipientid):
    content = request.POST['messagecontent']
    print(request.POST['hidden'])
    this_user=User.objects.get(id=request.POST['hidden'])
    this_recipient=User.objects.get(id=recipientid)
    Message.objects.create(content=content,user=this_user,recipient=this_recipient)
    redirectstr='/'+str(request.POST['hidden'])+'/show'
    return redirect(redirectstr)


def newcomment(request):
    content = request.POST['commentcontent']
    print(request.POST['hidden'])
    this_message=Message.objects.get(id=request.POST['hidden'])
    this_user=User.objects.get(id=request.POST['hidden2'])
    Comment.objects.create(content=content,message=this_message,ucomment=this_user)
    redirectstr='/'+str(request.POST['hidden2'])+'/show'
    return redirect(redirectstr)