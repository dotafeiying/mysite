#-*- coding: utf-8 -*-
from django import forms
# from .models import User
from django.contrib.auth.models import User

class LoginForm(forms.Form):
   username = forms.CharField(label='用户名',max_length = 100)
   password = forms.CharField(label='密码',widget = forms.PasswordInput())

   def clean_username(self):
       username = self.cleaned_data.get("username")
       dbuser = User.objects.filter(username=username)

       if not dbuser:
           raise forms.ValidationError(("User does not exist in our db!"),code='invalid')
       return username

   # def clean(self):
   #     if not self.is_valid():
   #         raise forms.ValidationError(u"用户名和密码为必填项")
   #     else:
   #         cleaned_data = super(LoginForm, self).clean()