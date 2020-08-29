from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json


from .forms import RegisterForm, CustomUserChangeForm

from .models import Jobs, Contest, Articles, Like

from .filters import JobFilter
# @login_required


# 메인 화면(임시)
def main_view(request):
    return render(request, "blog/main_view.html", )


# view
def set_view(request, model_name, field_name, path, page_name):
    obj = model_name.objects.filter(field=field_name)
    paginator = Paginator(obj, 10)
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/{path}/{path}_detail_list.html".format(path=path), {"posts": posts, "page_name":page_name})


# 뉴스
def article_list(request):
    return render(request, "blog/article/article_list.html", "뉴스")


def article_dev_list(request):
    return set_view(request, Articles, "개발자", "article", "개발자 뉴스")


def article_cloud_list(request):
    return set_view(request, Articles, "클라우드", "article", "클라우드 뉴스")

def article_big_data_list(request):
    return set_view(request, Articles, "빅데이터", "article", "빅데이터 뉴스")

def article_AI_list(request):
    return set_view(request, Articles, "AI", "article", "AI 뉴스")

def article_IoT_list(request):
    return set_view(request, Articles, "IoT", "article", "IoT 뉴스")

def article_devops_list(request):
    return set_view(request, Articles, "DevOps", "article", "DevOps 뉴스")

def article_secure_list(request):
    return set_view(request, Articles, "보안", "article", "보안 뉴스")    

def article_new_tech_list(request):
    return set_view(request, Articles, "신기술", "article", "신기술 뉴스") 


def trend(request):
    return render(request, "blog/trend/trend.html",)


# 채용공고

def job_list(request):
    
    posts = Jobs.objects.all()
    job_filter = JobFilter(request.GET, queryset=posts)

    return render(request, "blog/job/job_detail_list.html", {"posts": posts, "page_name":"채용공고", 'filter':job_filter})


def job_python_list(request):
    return set_view(request, Jobs, "", "job", "파이썬 채용공고")


def job_cloud_list(request):
    return set_view(request, Jobs, "cloud", "job", "클라우드 채용공고")


def job_db_list(request):
    return set_view(request, Jobs, "db", "job", "DB 채용공고")


# 공모전

def contest_set_view(request, model_name, field_name, page_name):
    obj = model_name.objects.filter(field=field_name)

    first = obj.order_by('-contest_views')[0]
    second = obj.order_by('-contest_views')[1]
    third = obj.order_by('-contest_views')[2]

    return render(request, "blog/contest/contest_detail_list.html",
                  {"contests": obj, "page_name": page_name, "first": first, "second": second, "third": third})


def contest_list(request):
    contest = Contest.objects.all()
    first = Contest.objects.order_by('-contest_views')[0]
    second = Contest.objects.order_by('-contest_views')[1]
    third = Contest.objects.order_by('-contest_views')[2]

    return render(request, "blog/contest/contest_detail_list.html",
                  {"contests": contest, "page_name": "공모전", "first": first, "second": second, "third": third})


def contest_game_list(request):
    return contest_set_view(request, Contest, '게임/소프트웨어', '게임/소프트웨어')

def contest_science_list(request):
    return contest_set_view(request, Contest, '과학/공학', '과학/공학')

def contest_job_list(request):
    return contest_set_view(request, Contest, '취업/창업', '취업/창업')

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            # 회원가입 폼의 데이터를 DB에 저장하는 코드를 user 라는 변수에 저장
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user)
            return render(request, 'registration/signup_done.html', {'user': user})

    elif request.method == 'GET':
        user_form = RegisterForm()
    
    if request.user.is_authenticated:
        return redirect('main_view')

    if request.user.is_authenticated:
        return redirect('main_view')

    return render(request, 'registration/signup.html', {'user_form': user_form})

@login_required
def update(request):
    if request.method=='POST':
        user=request.user

        gender = request.POST.get('성별')
        email= request.POST.get('email')
        phone = request.POST.get('휴대폰번호')
        first_interest = request.POST.get('관심사1')
        second_interest = request.POST.get('관심사2')

        user.성별 = gender
        user.email = email
        user.휴대폰번호 = phone
        user.관심사1 = first_interest
        user.관심사2 = second_interest

        user.save()
        return render(request,'blog/main_view.html',{'user':user})

    else:
        user_change_form=CustomUserChangeForm(instance=request.user)
        return render(request, 'registration/update.html', {'user_change_form': user_change_form})


def mypage(request):
    return render(request, 'blog/mypage.html')


@login_required
# @require_POST # 해당 뷰는 POST method 만 받는다.
def articles_like(request, articles_id):
    user = request.user  # 로그인된 유저 객체를 가져오기
    article = get_object_or_404(Articles, pk=articles_id)
    # article라는 변수 안에 게시물들 중에 article_id 를 pk를 기준으로 선별해서 하나의 게시물을 가져오기
    articles_like, articles_like_created=article.like_set.get_or_create(user=request.user)
    # 가져온 게시물의 like 값을 가져오거나 가져온 게시물의 like 값을 새로 만듭니다 이때 like의 user값은 현재 요청한 user로 설정합니다
    if not articles_like_created:
        articles_like.delete()
        #게시물의 like가 새로 만들어지 지지 않으면 가져온 게시물의 like 값을 삭제합니다
        return redirect('/article/'+str(article.id))
    return redirect('/article/' + str(article.id))