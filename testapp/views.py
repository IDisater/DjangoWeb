# coding=utf-8
import hashlib
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from testapp import models
import json,datetime
from django.db.models import Count
from django.core import serializers
from .models import User,Company,Information,Relationship,Collection,C_collection
from .forms import UserForm,RegisterForm,CompanyForm1,InformationForm,UserForm1,CpForm,CompanyForm,ComForm
from django.urls import reverse
from django.contrib import auth
from django import forms
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
def page_not_found(request):
    return render_to_response('404.html')
def page_error(request):

    return render_to_response('500.html')

def index(request):
    sam=models.Information.objects.order_by('?')[:20]#随机
    info1=models.Information.objects.order_by('-createdate')[:3]#最新
    info_hot=models.Information.objects.order_by('-views')[:3]#热度
    info=models.Information.objects.filter(is_hot='yes')[:3]#是否首页轮播
    return render(request, 'index.html',locals())
def test(request):
    return render(request,'bar-simple.html')
def cp_index(request):
    cp_name = request.session['cp_name']
    cp_title = request.session['cp_title']
    # 一年前的今天
    start = datetime.datetime.now() - relativedelta(months=12)
    # 当前时间
    now = datetime.datetime.now()
    # 获取近一年内数据
    data = C_collection.objects.filter(c_time__range=(start, now))
    res = data.extra(select={'day': 'day(c_time)'}).values('day').annotate(
        count=Count('c_time')).order_by()
    res_count=[]
    # for i in res:
    #     res_count.append(i['count'])
    q = 0
    for x in res_count:
        q+=x
    #time = datetime.strptime(start, "%Y/%m/%d")
    #print(type(start.year),type(start.month),type(start.day))
    #print(time)
    date_time=[]
    print(res)
    for m in range(0,7):
        t_day=now.day-m
        # for i in res:
        #     if i['day']==t_day:
        #         res_count.append(i['count'])
        #         continue
        #     else:
        #         res_count.append(0)
        #         break
        time=now.month+(now.day-m)*0.01
        date_time.append(time)
    d_time=date_time[::-1]
    print(d_time,res_count)
    # res = data.extra(select={'year': 'year(c_time)', 'month': 'month(c_time)', 'day': 'day(c_time)'}).values('year','month',                                                                                         'day').annotate(
    #     count=Count('c_time')).order_by()
    # res_data = []
    # print(res)
    # for item in res:
    #     month = str(item.get('month')) if item.get('month') > 9 else '0' + str(item.get('month'))
    #     res_data.append({
    #         'date': str(item.get('year')) + '-' + month,
    #         'count': item.get('count')
    #     })
    #     print()

    # def sortList(item):
    #     return item.get('date')
    # res_data.sort(key=sortList)
    #print(res.values('day'))
    # res_day=[]
    #
    #
    # res_count=[]
    # for i in res:
    #    print(i)
    #    res_i=list[]
    #    res_i
        #print(i.day,i.count)
    #print(res.__dict__['day'])
    #ap_info=models.C_collection.objects.all().filter(cp_title=cp_title).values()

    #print(json_data)


    cp_info = models.Company.objects.filter(cp_name=cp_name)
    return render(request,'cp_index.html',locals())
def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            user_name = login_form.cleaned_data['user_name']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(user_name=user_name)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_name'] = user.user_name
                    request.session['user_title'] = user.user_title
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())
def cp_login(request):
    if request.session.get('cpis_login', None):
        return redirect('/cp_index')
    if request.method == "POST":
        cplogin_form = CpForm(request.POST)
        message = "请检查填写的内容！"
        if cplogin_form.is_valid():
            cp_name = cplogin_form.cleaned_data['cp_name']
            password = cplogin_form.cleaned_data['password']
            try:
                cp = models.Company.objects.get(cp_name=cp_name)
                if cp.password == hash_code(password):
                    request.session['cpis_login'] = True
                    request.session['cp_name'] = cp.cp_name
                    request.session['cp_title'] = cp.cp_title
                    return redirect('/cp_index/')
                else:
                    print(hash_code(cp.password))
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'cp_login.html', locals())
    cplogin_form = CpForm()
    return render(request, 'cp_login.html', locals())
def register(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            user_name = register_form.cleaned_data['user_name']
            user_title=register_form.cleaned_data['user_title']
            password = register_form.cleaned_data['password']
            password1 = register_form.cleaned_data['password1']
            user_email = register_form.cleaned_data['user_email']
            user_sex = register_form.cleaned_data['user_sex']
            if password != password1:
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(user_name=user_name)
                if same_name_user:
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(user_email=user_email)
                if same_email_user:
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())
                new_user = models.User.objects.create()
                new_user.user_name = user_name
                new_user.password = hash_code(password)
                new_user.user_email = user_email
                new_user.user_sex = user_sex
                new_user.save()
                print(password,password1)
                succ='注册成功'
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())
def cp_register(request):
    if request.session.get('cpis_login', None):
        return redirect("/index/")
    if request.method == "POST":
        cpregister_form = CompanyForm(request.POST)
        message = "请检查填写的内容！"
        if cpregister_form.is_valid():
            cp_name = cpregister_form.cleaned_data['cp_name']
            cp_title=cpregister_form.cleaned_data['cp_title']
            password = cpregister_form.cleaned_data['password']
            password1 = cpregister_form.cleaned_data['password1']
            cp_email = cpregister_form.cleaned_data['cp_email']
            cp_tel= cpregister_form.cleaned_data['cp_tel']
            cp_address= cpregister_form.cleaned_data['cp_address']
            cp_about= cpregister_form.cleaned_data['cp_about']
            if password != password1:
                message = "两次输入的密码不同！"
                return render(request, 'cp_register.html', locals())
            else:
                same_name_cp = models.Company.objects.filter(cp_name=cp_name)
                if same_name_cp:
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'cp_register.html', locals())
                same_title_cp = models.Company.objects.filter(cp_title=cp_title)
                if same_title_cp:
                    message = '公司已经存在，请重新选择公司名！'
                    return render(request, 'cp_register.html', locals())
                same_email_cp = models.Company.objects.filter(cp_email=cp_email)
                if same_email_cp:
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'cp_register.html', locals())
                new_cp = models.Company.objects.create()
                new_cp.cp_name = cp_name
                new_cp.cp_title = cp_title
                new_cp.password = hash_code(password)
                new_cp.cp_email = cp_email
                new_cp.cp_tel=cp_tel
                new_cp.cp_address=cp_address
                new_cp.cp_about=cp_about
                new_cp.save()
                succ = '注册成功'
                return redirect('/cplogin/')
    cpregister_form = CompanyForm()
    return render(request, 'cp_register.html', locals())
def addinfo(request,cp_name):
    if request.method == "POST":
        add_form=InformationForm(request.POST,request.FILES)
        if add_form.is_valid():
            job=add_form.cleaned_data['job']
            cp_title = add_form.cleaned_data['cp_title']
            cp_email = add_form.cleaned_data['cp_email']
            cp_tel = add_form.cleaned_data['cp_tel']
            cp_address = add_form.cleaned_data['cp_address']
            classes = add_form.cleaned_data['classes']
            info=add_form.cleaned_data['info']
            pay=add_form.cleaned_data['pay']
            info_img=add_form.cleaned_data['info_img']
            new_info=models.Information.objects.create()
            new_info.cp_title=cp_title
            new_info.job=job
            new_info.classes=classes
            new_info.info=info
            new_info.pay=pay
            new_info.info_img=info_img
            new_info.cp_email = cp_email
            new_info.cp_tel = cp_tel
            new_info.cp_address= cp_address
            new_info.save()
            succ='发布成功'
            return render(request,'add_info.html',locals())
        return render(request,'add_info.html',locals())
    add_info = models.Company.objects.filter(cp_name=cp_name)
    return render(request, 'add_info.html', locals())
def logout(request):
    if not request.session.get('cpis_login', None) and not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")
def C_change(request):
    cp_name=request.GET.get('cp_name')
    if request.method == "POST":
        change_form = CompanyForm(request.POST, request.FILES)
        if change_form.is_valid():
            cp_title=change_form.cleaned_data['cp_title']
            cp_email = change_form.cleaned_data['cp_email']
            cp_tel = change_form.cleaned_data['cp_tle']
            cp_address = change_form.cleaned_data['cp_address']
            cp_about = change_form.cleaned_data['cp_about']
            models.Company.objects.filter(cp_name=cp_name).update(cp_title=cp_title,
            cp_email=cp_email,cp_tel=cp_tel,cp_address=cp_address,cp_about=cp_about)
            succ='修改成功'
    cp_list=models.Company.objects.filter(cp_name=cp_name)
    return render(request,'c_change.html',locals())
def Change_o(request,user_name):
    if request.method == "POST":
        change_form = UserForm1(request.POST,request.FILES)
        if change_form.is_valid():
            user_title=change_form.cleaned_data['user_title']
            user_sex=change_form.cleaned_data['user_sex']
            user_email=change_form.cleaned_data['user_email']
            user_tel=change_form.cleaned_data['user_tel']
            address=change_form.cleaned_data['address']
            user_about=change_form.cleaned_data['user_about']
            models.User.objects.filter(user_name=user_name).update(user_title=user_title,
            user_about=user_about,user_tel=user_tel,user_email=user_email,user_sex=
            user_sex,address=address)
            message = '修改成功'
    person_list = models.User.objects.filter(user_name=user_name)
    return render(request,'user-person.html',locals())
def Showdetails(request,info_id,user_name):
    info_form = models.Information.objects.filter(info_id=info_id)
    is_fav=models.Collection.objects.filter(user_name=user_name,info_id=info_id)
    is_apply=models.C_collection.objects.filter(user_name=user_name,info_id=info_id)
    is_say=models.Comments.objects.filter(user_name=user_name,info_id=info_id).order_by('-com_time')
    test=models.Information.objects.get(info_id=info_id)
    models.Information.objects.filter(info_id=info_id).update(views=(test.views+1))
    return render(request, 'details.html', locals())
def Classes(request,classes):
    infoclass=Information.objects.filter(classes=classes).order_by('-createdate')
    pindex = request.GET.get('pindex')
    p = Paginator(infoclass, 6)
    if pindex == ' ':
        pindex = 1
    else:
        int(pindex)
    page = p.page(pindex)
    return render(request,'classes.html',locals())
x = ''
def all_info(requset,cp_title):
    allinfo=models.Information.objects.filter(cp_title=cp_title).order_by('-createdate')
    pindex = requset.GET.get('pindex')
    p = Paginator(allinfo, 8)
    if pindex == ' ':
        pindex = 1
    else:
        int(pindex)
    page = p.page(pindex)
    return render(requset,'cp_allinfo.html',locals())
def Search(request,pindex):
    q = request.GET.get('q')
    post_list = models.Information.objects.filter(Q(cp_title__icontains=q) | Q(job__icontains=q))\
        .order_by('createdate')
    if q:
        request.session['q'] = q
        p = Paginator(post_list, 4)
        if pindex ==None:
            pindex = 1
        else:
            int(pindex)
        page = p.page(pindex)
        return render(request, 'search-details.html', locals())
    else:
        message='请输入关键字'
        return redirect('/index/')

def is_offer(request,user_name):
    offer=models.C_collection.objects.filter(user_name=user_name)
    return render(request,'is_apply.html',locals())
def Favorite(request,info_id,user_name):
    is_fav=models.Collection.objects.filter(info_id=info_id,user_name=user_name)
    if is_fav.exists()==False:
        add_fav=models.Information.objects.get(info_id=info_id)
        new_fav= models.Collection.objects.create()
        new_fav.job=add_fav.job
        new_fav.pay=add_fav.pay
        new_fav.cp_title=add_fav.cp_title
        new_fav.info_id=info_id
        new_fav.user_name=user_name
        new_fav.save()
        message='收藏成功'
        return Showdetails(request,info_id,user_name)
    else:
        return Showdetails(request,info_id,user_name)
def apply(request,info_id,user_name):
    is_apply=models.C_collection.objects.filter(info_id=info_id,user_name=user_name)
    if is_apply.exists()==False:
        user=models.User.objects.get(user_name=user_name)
        cp = models.Information.objects.get(info_id=info_id)
        new_apply=models.C_collection.objects.create()
        new_apply.user_titel=user.user_title
        new_apply.user_name=user.user_name
        new_apply.cp_title=cp.cp_title
        new_apply.job=cp.job
        new_apply.pay = cp.pay
        new_apply.info_id=info_id
        new_apply.save()
        succ='投递成功'
        return Showdetails(request,info_id,user_name)
    else:
        return Showdetails(request,info_id,user_name)
def Mylove(request,user_name):
    fav_form = models.Collection.objects.filter(user_name=user_name)\
        .order_by('-col_time')
    pindex = request.GET.get('pindex')
    p = Paginator(fav_form, 6)
    if pindex ==' ':
        pindex = 1
    else:
        int(pindex)
    page = p.page(pindex)
    return render(request,'mylove.html',locals())
def Info_mana(request,cp_title):
    mana_form = models.C_collection.objects.filter(cp_title=cp_title).order_by('-c_time')
    pindex = request.GET.get('pindex')
    p=Paginator(mana_form,8)
    if pindex==' ' :
        pindex=1
    else:
        int(pindex)
    page=p.page(pindex)
    return render(request,'cp_mana.html',locals())
def del_info(request,info_id,cp_title):
    cls_form=models.Information.objects.filter(info_id=info_id).delete()
    return Info_mana(request,cp_title)
def show_o(request,user_name):
    user=models.User.objects.filter(user_name=user_name)
    models.C_collection.objects.filter(user_name=user_name).update(is_look='yes')
    return render(request,'person.html',locals())
def add_say(request):
    user_name=request.GET.get('user_name')
    info_id = request.GET.get('info_id')
    com_about = request.GET.get('com_about')
    user=models.User.objects.get(user_name=user_name)
    new_say=models.Comments.objects.create()
    new_say.info_id=info_id
    new_say.user_name=user_name
    new_say.user_title=user.user_title
    new_say.com_about=com_about
    new_say.save()
    return Showdetails(request,info_id,user_name)
def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()