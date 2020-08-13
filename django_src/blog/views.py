from django.shortcuts import render,  get_object_or_404

from .models import News

def main_view(request):
    return render(request, "blog/main_view.html",)

def article_new_tech_list(request):
    articles = News.objects.all()

    return render(request, "blog/article_new_tech_list.html", {"articles": articles})