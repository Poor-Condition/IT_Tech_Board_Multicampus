from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.db.models import Max

from .forms import RegisterForm

from .models import Jobs, Contest_game, Contest_job, Contest_science, Articles, Study

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
def contest_list(request):
    return render(request, "blog/contest/contest_list.html",)


def contest_game_list(request):
    contest_game = Contest_game.objects.all()
    first = Contest_game.objects.order_by('-contest_views')[0]
    second = Contest_game.objects.order_by('-contest_views')[1]
    third = Contest_game.objects.order_by('-contest_views')[2]

    return render(request, "blog/contest/contest_detail_list.html", {"contests": contest_game, "page_name":"게임 공모전", "first":first, "second":second, "third":third})


def contest_science_list(request):
    contest_science = Contest_science.objects.all()
    first = Contest_science.objects.order_by('-contest_views')[0]
    second = Contest_science.objects.order_by('-contest_views')[1]
    third = Contest_science.objects.order_by('-contest_views')[2]

    return render(request, "blog/contest/contest_detail_list.html", {"contests": contest_science, "page_name":"과학 공모전", "first":first, "second":second, "third":third})


def contest_job_list(request):
    contest_job = Contest_job.objects.all()
    first = Contest_job.objects.order_by('-contest_views')[0]
    second = Contest_job.objects.order_by('-contest_views')[1]
    third = Contest_job.objects.order_by('-contest_views')[2]

    return render(request, "blog/contest/contest_detail_list.html", {"contests": contest_job, "page_name":"취업/창업 공모전", "first":first, "second":second, "third":third})


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


def study(request):
    studies = Study.objects.all()

    return render(request, "blog/job/job_detail_list.html", {"studies": studies, "page_name":"스터디"})