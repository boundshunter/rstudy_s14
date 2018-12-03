from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def login(request):
    error_msg = ""
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            return redirect('/home')
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})

USER_LIST = []

for item in range(20):
    temp = {'username': 'abc'+str(item), 'gender': '男', 'email': str(item)+'@123.com'}

    USER_LIST.append(temp)
print(USER_LIST)


def home(request):

    if request.method == 'POST':
        u = request.POST.get('user')
        g = request.POST.get('gender')
        e = request.POST.get('email')
        temp = {'username': u, 'gender': g, 'email': e}
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})


def upload(request):
    print(request.FILES.get('upload'))
    obj = request.FILES.get("upload")
    import os
    # 获取上传路径+文件名
    upload_path = os.path.join('upload', obj.name)
    f = open(upload_path, 'wb')
    for row in obj.chunks():
        # 将上传文件写入指定路径并指定文件名，这里使用默认上传的文件名
        f.write(row)
    f.close()
    return HttpResponse("上传成功")


from django.views import View

class Cbv(View):
    '''定义get和post方法执行函数'''

    # 实际上 调用的是dispatch
    def dispatch(self, request, *args, **kwargs):
        # 调用父类的dispatch
        # before ， after 可以设置一些自定义的东西
        print(before)
        result = super(Cbv, self).dispatch(request, *args, **kwargs)
        print(after)
        return result

    def get(self, request):
        print(request.method)
        return render(request, 'cbv.html')

    def post(self, request):
        print(request.method)
        return render(request, 'cbv.html')


USER_DICT = {
    '1': {'user': 'root1', 'email': 'root1@123.com'},
    '2': {'user': 'root2', 'email': 'root2@123.com'},
    '3': {'user': 'root3', 'email': 'root3@123.com'},
    '4': {'user': 'root4', 'email': 'root4@123.com'},
    '5': {'user': 'root5', 'email': 'root5@123.com'},
    '6': {'user': 'root6', 'email': 'root6@123.com'},
}


class List(View):
    def get(self, request):
        return render(request, 'list.html', {'user_dict': USER_DICT})


class Detail(View):
    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        nid = kwargs['nid']
        detail_info = USER_DICT[nid]
        return render(request, 'detail.html', {'args': args, 'kwargs': kwargs, 'detail_info': detail_info})

    def post(self, request, *args, **kwargs):
        pass
