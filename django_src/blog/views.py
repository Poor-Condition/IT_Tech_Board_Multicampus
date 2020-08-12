from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponseRedirect

from .models import News

def article_new_tech_list(request):
    articles = News.objects.all()

    return render(request, "blog/article_new_tech_list.html", {"articles": articles})