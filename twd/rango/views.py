# -*- coding:utf-8 -*-

from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Category, Page
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
from bing_search import run_query
# Create your views here.


def index(request):
    # request.session.set_test_cookie()
    category_all = Category.objects.all()
    category_t5 = Category.objects.order_by('-likes')[:5] #-likes,按照likes降序排列
    page_t5 = Page.objects.order_by('-likes')[:5]
    context_dict = {'category_t5': category_t5, 'page_t5':page_t5, 'category_all':category_all}
    # 获取访问次数,有的话是多少就是多少，没的话置为 1
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False
    # response = render(request, 'rango/index.html', context_dict)
    # session中是否存在上次访问时间,有的话获取。没有，获取到的是空
    last_visit = request.session.get('last_visit')
    if last_visit:
        # 是的 存在
        # 获取到指定格式的last_visit_time用于后面计算
        last_visit_time = datetime.strptime(last_visit[:-7], '%Y-%m-%d %H:%M:%S')
        # print 'last_visit_time', last_visit_time, 'now', datetime.now()
        # 距离上次访问超过一天了吗
        if (datetime.now() - last_visit_time).seconds > 0:
            # print (datetime.now() - last_visit_time).seconds
            visits += 1
            # 是的，那么访问次数 + 1，同时更新标记置为True
            reset_last_visit_time = True
    else:
        # no，不存在，那么该重置时间了
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits

    context_dict['visits'] = visits
    # 早一步设置好，后面设置cookie的时候就可以使用里面的信息了
    response = render(request, 'rango/index.html', context_dict)



    return response


def category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def about(request):
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    return render(request, 'rango/about.html', {'visits': visits})


def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request, 'rango/add_catrgory.html', {'form': form})


def add_page(request, category_name_slug):

    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
                cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.save()
                # probably better to use a redirect here.
                return redirect('/rango/category/'+cat.slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': cat}

    return render(request, 'rango/add_page.html', context_dict)


def register(request):
    # if request.session.test_cookie_worked():
    #     print '>>> TEST COOKIE WORKED!'
    #     request.session.delete_test_cookie()
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                  {'user_form': user_form, 'profile_form': profile_form,
                   'registered': registered
                   })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('/rango/')
            else:
                return HttpResponse('Your Rango account is disabled!')
        else:
            print 'Incalid login details: {}, {}'.format(username, password)
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/rango/')


@login_required
def restricted(request):
            return render(request, 'rango/restricted.html', {})


def search(request):
    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})
