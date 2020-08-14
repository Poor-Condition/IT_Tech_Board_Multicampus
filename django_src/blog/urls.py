from django.urls import path
from . import views

urlpatterns = [
    #뉴스
    path('', views.main_view, name='main_view'),
    path('article', views.article_list, name='article_list'),
    path('article/article_dev/', views.article_dev_list, name='article_dev_list'),
    path('article/article_cloud/', views.article_cloud_list, name='article_cloud_list'),
    path('article/article_new_tech/', views.article_new_tech_list, name='article_new_tech_list'),

    # 공모전
    path('', views.main_view, name='main_view'),
    path('contest', views.contest_list, name='contest_list'),
    path('contest/contest_game/', views.contest_game_list, name='contest_game_list'),
    path('contest/contest_science/', views.contest_science_list, name='contest_science_list'),
    path('contest/contest_job/', views.contest_job_list, name='contest_job_list')

]