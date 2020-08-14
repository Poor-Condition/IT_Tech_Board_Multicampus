from django.shortcuts import render,  get_object_or_404

from .models import News_dev, News_cloud, News_new_tech, Contest_game, Contest_job, Contest_science

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


