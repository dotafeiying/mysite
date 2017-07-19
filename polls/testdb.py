# -*- coding: utf-8 -*-
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()
from polls.models import Question,Choice
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import resolve

# datas=Question.objects.all()
# print(datas)
# datas1=Question.objects.filter(question_text__startswith='')
# print(datas1)
# q = Question.objects.get(pk=1)
# print(q)
# q.choice_set.create(choice_text='Not much', votes=0)
#
# print(q.choice_set.all())
# q=Choice(question_id=3,choice_text='xulu',votes=1)
# q.save()
# print(Choice.objects.all())

# q = Question(question_text="What's up?", pub_date=timezone.now())
# q.save()
# q=Question.objects.order_by('pub_date')[:5]
# print(q)
user_obj = User.objects.get(username='yuanjie')
print(dir(user_obj))
p=user_obj.get_all_permissions()
print(p)
print(user_obj.check_password('yj123456'))

