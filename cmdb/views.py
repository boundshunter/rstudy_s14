from django.shortcuts import render, HttpResponse, redirect
from cmdb import models
# Create your views here.


def login(request):
    # 判断提交方式
    err_msg = ""
    print(request.method)
    if request.method == 'POST':
        # 通过POST参数获取提交的数据
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # 判断提交过来的数据，通过数据库查询，是否为空，不为空则存在,取获取到的第一个
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        # 第二种获取方式, count=0 则为空，不存在，判断count 是否为0 , 0 为 None
        # obj = models.UserInfo.objects.filter(username=u, password=p).count()
        if obj: # Not None
            user_dic = {"username": u}
            return render(request, 'enter.html', {'user_dic': user_dic})
        else:
            err_msg = "用户名或密码错误"
    return render(request, 'cmdblogin.html', {'err_msg': err_msg})


def orm(request):
    # 创建数据，三种方式
    # 一:
    # models.UserInfo.objects.create(username='jjj', password='ccc')
    # 二:
    # dic = {'username': 'kkk', 'password': 'kkk'}
    # models.UserInfo.objects.create(**dic)
    # 三:
    obj = models.UserInfo(username='obj', password='obj')
    obj.save()
    return HttpResponse('数据创建成功')


def userinfo(request):
    if request.method == "GET":
        obj = models.UserInfo.objects.all()
        return render(request, 'userinfo.html', {'user_list': obj})
    if request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        print(u,p)
        models.UserInfo.objects.create(username=u, password=p)
        return redirect('/cmdb/userinfo/')

def usergroup(request):
    return HttpResponse("usergroup")


def userdetail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request, 'userdetail.html', {'obj': obj})


def useredit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'useredit.html', {'obj': obj})
    if request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p)
        return redirect('/cmdb/userinfo/')

def userdel(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/userinfo/')