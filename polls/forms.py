#-*- coding: utf-8 -*-
from django import forms
# from .models import User
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length = 100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入用户名"}))
    password = forms.CharField(label='密码',
        widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':"请输入密码"}))

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

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label=u'原始密码',error_messages={'required':'请输入原始密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=u'新密码',error_messages={'required':'请输入新密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=u'重复输入',error_messages={'required':'请重复新输入密码'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(u'原密码错误')
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if len(password1)<6:
            raise forms.ValidationError(u'密码必须大于6位')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(u'两次密码输入不一致')
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user