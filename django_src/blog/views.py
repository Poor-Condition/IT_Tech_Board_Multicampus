from django.contrib.auth import login
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View
from django.db.models import Max
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.views.decorators.http import require_POST


from .forms import RegisterForm, CustomUserChangeForm, CreateStudyForm

from .models import Jobs, Contest, Articles, User, Study

from .filters import JobFilter
# @login_required


# 메인 화면(임시)
def main_view(request):
    return render(request, "blog/main_view.html", )

#메인 화면 검색
def main_search(request):
    q = request.GET['search_query']
    articles = Articles.objects.filter(news_title__icontains=q)[0:5]
    contests = Contest.objects.filter(contest_title__icontains=q)[0:5]
    jobs = Jobs.objects.filter(Q(job_title__icontains=q) | Q(company__icontains=q))[0:5]
    return render(request, "blog/main_search.html", {'articles':articles, 'contests':contests, 'jobs':jobs, 'page_name':'검색 결과', 'q':q})


# view
def set_view(request, model_name, field_name, path, page_name):
    obj = model_name.objects.filter(field=field_name)
    paginator = Paginator(obj, 10)
    page = request.GET.get("page", 1)

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/{path}/{path}_detail_list.html".format(path=path), {"posts": posts, "page_name":page_name, "page":page})


# 뉴스
def article_list(request):
    obj = Articles.objects.all()
    paginator = Paginator(obj, 10)
    page = request.GET.get("page", 1)

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/article/article_detail_list.html', {"posts": posts, "page_name":"뉴스", "page":page})


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
    
    job_list = Jobs.objects.all()
    job_filter = JobFilter(request.GET, queryset=job_list)
    job_list = job_filter.qs

    paginator = Paginator(job_list, 10)
    page = request.GET.get("page", 1)

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/job/job_detail_list.html", {"posts": posts, "page_name":"채용공고", 'paginator': paginator, 'filter':job_filter, 'page':page})


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

    return render(request, 'registration/signup.html', {'user_form': user_form})

def study_chat(request):
    return render(request, "chat/chat.html", {})

def room(request, room_name):
    study = Study.objects.get(pk=room_name)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'study':study
    })

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

@login_required
def mypage(request):
    user = request.user
    studies = Study.objects.filter(members=user)[0:3]
    return render(request, 'blog/mypage.html', {'studies':studies, "page_name":"My Page"})


@login_required
def create_study(request):
    form = CreateStudyForm(request.POST)
    if request.method == 'POST':
        user = request.user
        if form.is_valid():
            form.instance.owner = user
            post = form.save(commit=False)
            post.save()
            form.instance.members.add(user)
            return redirect('study')
    return render(request, 'blog/study/create_study.html', {'form':form})

def study(request):
    studies = Study.objects.all()
    return render(request, 'blog/study/study.html', {'studies':studies, "page_name":"스터디"})

def my_study(request):
    user = request.user
    studies = Study.objects.filter(members=user)

    return render(request, 'blog/study/my_study.html', {'studies':studies, "page_name":"스터디"})

@login_required
def cancel_study(request, id):
    user = request.user
    study = Study.objects.get(pk=id)
    if user == study.owner:
        study.delete()
    else:
        study.members.remove(user)
    return render(request, 'blog/study/cancel_study.html', {"page_name":"스터디"})

@login_required
def join_study(request, id):
    user = request.user
    study = Study.objects.get(pk=id)

    if study.members.count() >= study.max_member:
        return render(request, 'blog/study/max.html')
    else:
        study.members.add(user)
    return render(request, 'blog/study/join_study.html', {"page_name":"스터디"})

@login_required
@require_POST
def article_like(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    user = request.user

    check_like_post = article.article_likes.filter(id=user.id)

    if check_like_post.exists():
        article.article_likes.remove(user.id)
        article.article_like_count -= 1
        article.save()
    else:
        article.article_likes.add(user.id)
        article.article_like_count += 1
        article.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
@require_POST
def contest_like(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    user = request.user

    check_like_post = contest.contest_likes.filter(id=user.id)

    if check_like_post.exists():
        contest.contest_likes.remove(user.id)
        contest.contest_like_count -= 1
        contest.save()
    else:
        contest.contest_likes.add(user.id)
        contest.contest_like_count += 1
        contest.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





@login_required
@require_POST
def job_like(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)
    user = request.user
    # profile = User.objects.get(id=user.id)

    check_like_post = job.job_likes.filter(id=user.id)

    if check_like_post.exists():
        job.job_likes.remove(user.id)
        job.job_like_count -= 1
        job.save()
    else:
        job.job_likes.add(user.id)
        job.job_like_count += 1
        job.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))