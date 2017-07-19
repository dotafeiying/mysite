from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect,render_to_response
from .models import Question,Choice,User
from django.urls import reverse
from django.views.generic import ListView,DetailView
from .forms import LoginForm,ChangePasswordForm
from django.contrib import auth
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import resolve
from .permission import check_permission

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {}
#     context['latest_question_list'] = latest_question_list
#     return render(request,'polls/index.html',context)


# def hello(request):
#     context={}
#     context['name']='袁杰'
#     return render(request,'polls/hello.html',context)

# def detail(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{"question":question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，并给出提示信息
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交。
        # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        return redirect(reverse('polls:results', args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     print(question)
#     return render(request, 'polls/results.html', {'question': question})

class Indexview(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class Detailview(DetailView):
    model=Question
    template_name='polls/detail.html'

class Resultview(DetailView):
    model=Question
    template_name='polls/results.html'


def login(request):
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            # user = User.objects.filter(username__exact=username,password__exact=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                response=redirect(reverse('polls:success'))
                # response.set_cookie('username',username,3600)
                return response
                # return render_to_response('polls/success.html', {'username': username})
            else:
                return HttpResponseRedirect(reverse('polls:login'))
                # return redirect('polls:login')

                # username=MyLoginForm.user
            # print(username)
    else:
        MyLoginForm = LoginForm()

    return render(request, 'polls/login.html', {'form':MyLoginForm})

@login_required
# @check_permission
def success(request):
    # username=request.COOKIES.get('username','')
    # username=request.user
    # return render_to_response('polls/success.html',{'username':username})
    return render(request,'polls/success.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('polls:login')
    # return HttpResponse('sucess')

# @login_required
# @permission_required('polls.delete_user',raise_exception=True)
def home(request):
    return render(request,'polls/home.html')
    # return render_to_response('polls/home.html')

def about(request):
    return render(request,'polls/about.html')

@login_required
def ChangePassword(request):
    if request.method=='POST':
        form = ChangePasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:logout'))
    else:
        form = ChangePasswordForm(user=request.user)

    kwvars = {
        'form':form,
    }

    return render(request,'polls/password_change.html',kwvars)