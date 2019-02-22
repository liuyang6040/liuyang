from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from user.models import User
from django.core.cache import cache
import random
from utils.password import rsautil
from utils.loginmixin import LoginRequiredMixin
class LoginView(View):
    def get(self, request):
        '''显示登录页面'''
        return render(request, 'login.html')

    def post(self, request):
        '''校验登录页面'''
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = rsautil.decrypt_data(password)
        user = authenticate(request, username=username,
                            password=password)  # 拿着用户名密码去认证系统中校验用户名和密码是否正确，如果正确，返回user对象，将此对象写入到request中
        if user is not None:
            login(request, user)  # 将user对象注册到request中，后面所有需要登录后查看的页面可直接使用
            return JsonResponse({"retCode": 1, "retMsg": reverse('goods:index')})
        else:
            return JsonResponse({"retCode": 0, "retMsg": "用户名密码不匹配"})

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = rsautil.decrypt_data(password)
        phoneNo = request.POST.get("phoneNo")
        yzm = request.POST.get("yzm")
        cacheyzm = cache.get(phoneNo)
        if str(cacheyzm) != yzm:
            return JsonResponse({"retCode": 0, "retMsg": "验证码输入有误"})
        user = User.objects.filter(username=username)
        if len(user) > 0:
            return JsonResponse({"retCode": 0, "retMsg": "用户名已存在"})

        user = User.objects.create_user(username=username, password=password, phoneNo=phoneNo)
        user.save()
        # 返回应答, 跳转到首页
        return JsonResponse({"retCode": 1, "retMsg": reverse('user:login')})
#
class LogoutView(View):
    def get(self, request):
        '''退出登录'''
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('goods:index'))

class SmsView(View):
    def post(self, request):
        phoneNo = request.POST.get("phoneNo")
        exist = cache.get(phoneNo)  # 判断验证码是否存在，如果存在了，2分钟内，不让用户再次发送
        print(exist)
        if exist == None:
            cache.set(phoneNo, random.randint(100000, 1000000), 300)  # 生成6位的随机验证码
            # smsroute 异步写入
            return JsonResponse({"retCode": 1})
        else:
            return JsonResponse({"retCode": 0})

class UserView(LoginRequiredMixin, View):
    def get(self, request):
        '''显示'''
        # Django会给request对象添加一个属性request.user
        # 如果用户未登录->user是AnonymousUser类的一个实例对象
        # 如果用户登录->user是User类的一个实例对象
        # request.user.is_authenticated()

        # 获取用户的个人信息
        user = request.user

        # 组织上下文

        # 除了你给模板文件传递的模板变量之外，django框架会把request.user也传给模板文件
        return render(request, 'user_center_info.html')
class CheckUserView(View):
    def get(self, request):
        username = request.GET.get("username")
        user = User.objects.filter(username=username)
        if len(user) > 0:
            return JsonResponse({"retCode": 1})
        else:
            return JsonResponse({"retCode": 0})