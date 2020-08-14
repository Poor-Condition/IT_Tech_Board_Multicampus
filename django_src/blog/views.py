from django.shortcuts import render,  get_object_or_404

from .models import News_dev, News_cloud, News_new_tech

def main_view(request):
    return render(request, "blog/main_view.html",)

def article_list(request):
    return render(request, "blog/article/article_list.html",)

def article_dev_list(request):
    article_dev = News_dev.objects.all()

    return render(request, "blog/article/article_detail_list.html", {"articles": article_dev})

def article_cloud_list(request):
    article_cloud = News_cloud.objects.all()

    return render(request, "blog/article/article_detail_list.html", {"articles": article_cloud})

def article_new_tech_list(request):
    article_new_tech = News_new_tech.objects.all()

    return render(request, "blog/article/article_detail_list.html", {"articles": article_new_tech})