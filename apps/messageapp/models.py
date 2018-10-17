from __future__ import unicode_literals
from django.db import models
import bcrypt
from ..users.models import *
class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['messagecontent']) < 2:
            errors["content"] = "content cannot be less than 2 characters"
        if len(postData['messagecontent']) > 140:
            errors["content"] = "message cannot be over 140 characters" #ADD MAX LENGTH VALIDATIONS OM ALL
        return errors
class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['commentcontent']) < 2:
            errors["content"] = "content cannot be less than 2 characters"
        if len(postData['commentcontent']) > 140:
            errors["content"] = "Comment cannot be over 140 characters" #ADD MAX LENGTH VALIDATIONS OM ALL
        return errors
class Message(models.Model):
    user=models.ForeignKey(User, related_name="author")
    recipient=models.ForeignKey(User, related_name='message_recipient')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments")
    ucomment=models.ForeignKey(User, related_name='ucomments')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
