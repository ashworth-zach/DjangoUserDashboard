from __future__ import unicode_literals
from django.db import models
import bcrypt
from ..users.models import *

# Create your models here.
class Message(models.Model):
    user=models.ForeignKey(User, related_name="userhasmessages")
    recipient=models.ForeignKey(User, related_name='message_recipient')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments")
    ucomment=models.ForeignKey(User, related_name='ucomments')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)