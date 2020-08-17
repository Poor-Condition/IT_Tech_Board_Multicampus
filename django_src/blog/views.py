from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .models import News_dev, News_cloud, News_new_tech, Jobs_DB, Jobs_Cloud, Jobs_Python, Contest_game, Contest_job, Contest_science, Articles
from .forms import RegisterForm

# 메인 화면(임시)
def main_view(request):
    return render(request, "blog/main_view.html", )

# view
def set_view(request, model_name, field_name, path):
    obj = model_name.objects.filter(field=field_name)
    paginator = Paginator(obj, 10)
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/{path}/{path}_detail_list.html".format(path=path), {"posts": posts})

# 뉴스
def article_list(request):
    return render(request, "blog/article/article_list.html", )

def article_dev_list(request):
    return set_view(request, Articles, "개발자", "article")


def article_cloud_list(request):
    return set_view(request, Articles, "클라우드", "article")

def article_new_tech_list(request):
    return set_view(request, Articles, "신기술", "article")

# 채용공고
def job_list(request):
    return render(request, "blog/job/job_list.html",)

def job_python_list(request):
    jobs_python = Jobs_Python.objects.all()
    return render(request, "blog/job/job_detail_list.html", {"jobs": jobs_python})


def job_cloud_list(request):
    jobs_cloud = Jobs_Cloud.objects.all()

    return render(request, "blog/job/job_detail_list.html", {"jobs": jobs_cloud})

def job_db_list(request):
    jobs_db = Jobs_DB.objects.all()

    return render(request, "blog/job/job_detail_list.html", {"jobs": jobs_db})


# 공모전
def contest_list(request):
    return render(request, "blog/contest/contest_list.html",)

def contest_game_list(request):
    contest_game = Contest_game.objects.all()

    return render(request, "blog/contest/contest_detail_list.html", {"contests": contest_game})

def contest_science_list(request):
    contest_science = Contest_science.objects.all()

    return render(request, "blog/contest/contest_detail_list.html", {"contests": contest_science})

def contest_job_list(request):
    contest_job = Contest_job.objects.all()

    return render(request, "blog/contest/contest_detail_list.html", {"contests": contest_job})

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/signup_done.html', {'user': user})

    elif request.method == 'GET':
        user_form = RegisterForm()

    return render(request, 'registration/signup.html', {'user_form': user_form})