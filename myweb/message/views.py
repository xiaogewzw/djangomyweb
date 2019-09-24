from django.shortcuts import render , redirect
from django.http import HttpResponse
from message.models import User , Message
from django.utils import timezone


def index(request):
    message_list = Message.objects.all()


    context = {
        'message_list' : message_list,
    }

    return render(request,'message/index.html' , context)

def login(request):
    #message = request.POST.get('message' , '')
    #message = request.POST['message']
    if request.method == "POST":
        login_username = request.POST['username']
        login_password = request.POST['password']
        user_list = User.objects.all()
        b = True
        for a in user_list:
            if login_username == a.username:
                b = False
                if login_password == a.password:
                    #登录成功使用session记录登录用户的id
                    #用户处于登录状态，退出浏览器后失效
                    request.session['is_login'] = True
                    request.session['user_id'] = a.id
                    request.session.set_expiry(0)
                    return redirect('/message/userinterface/')
                else:
                    #错误：提示密码错误
                    context = {
                        'text' : '密码错误！！！',
                    }
                    return render(request , 'message/login.html' , context)
        if b:
            #错误：提示账号不存在
            context = {
                'text' : '该账号不存在，请先注册！',
            }
            return render(request , 'message/login.html' , context)
    else:
        return render(request , 'message/login.html')

def register(request):
    if request.method == "POST":
        register_username = request.POST.get('username' , '')
        register_password = request.POST.get('password' , '')
        #判断条件
        c = True
        #1、不能注册名字相同的账号

        user_list = User.objects.all()
        username_list = []
        for b in user_list:
            username_list.append(b.username)
        for d in username_list:
            if register_username == d:
                c = False

        #符合规定c为True，成功注册
        if c:
            a = User()
            a.username = register_username
            a.password = register_password 
            a.creation_time = timezone.now()
            a.save()
            context = {
                'text' : '你已经注册成功，即可登录!',
            }
            return render(request , 'message/login.html' , context)
        #不符合规定重新注册
        else:
            context = {
                'text' : '你输入的账号已经存在，请你换个账号名！！！',
            }
            return render(request , 'message/register.html' , context)
    else:
        return render(request , 'message/register.html')


def userinterface(request):
    if request.session['is_login']:
        #写留言的情况
        if request.method =="POST":
            #确认用户的id
            user_id = request.session['user_id']
            username = User.objects.get(id = user_id)
            #获取该用户的留言
            user_message_list = Message.objects.filter(message_user = username)

            #填写留言
            a = Message()
            a.message_text = request.POST.get('message_text' , '')
            a.message_contect = request.POST.get('message_contect' , '')
            a.message_user = User.objects.get(id = user_id)
            a.message_time =timezone.now()
            a.save()

            context = {
                'user_message_list' : user_message_list,
            }
            return render(request , 'message/userinterface.html' , context)
        else:
            #确认用户的id
            user_id = request.session['user_id']
            username = User.objects.get(id = user_id)
            #获取该用户的留言
            user_message_list = Message.objects.filter(message_user = username)

            context = {
                'user_message_list' : user_message_list,
            }
            return render(request , 'message/userinterface.html' , context)
    else:
        context = {
            'error' : '你还没有登陆，请先登录！',
        }
        return render(request , 'message/login.html' , context)

def messagedetail(request , message_id):
    message = Message.objects.get(id = message_id)
    context = {
        'message' : message,
    }
    return render(request , 'message/messagedetail.html' , context)
