from django.shortcuts import render,  get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News_dev, News_cloud, News_new_tech

def main_view(request):
    return render(request, "blog/main_view.html",)

def article_list(request):
    return render(request, "blog/article/article_list.html",)

def article_dev_list(request):
    article_dev = News_dev.objects.all()
    paginator = Paginator(article_dev, 10)
    page = request.GET.get("page")

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog/article/article_detail_list.html", {"posts": posts})

def article_cloud_list(request):
    article_cloud = News_cloud.objects.all()
    paginator = Paginator(article_cloud, 10)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(request, "blog/article/article_detail_list.html", {"posts": posts})

def article_new_tech_list(request):
    article_new_tech = News_new_tech.objects.all()
    paginator = Paginator(article_new_tech, 10)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    
    return render(request, "blog/article/article_detail_list.html", {"posts": posts})