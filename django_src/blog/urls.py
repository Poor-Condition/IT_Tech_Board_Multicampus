from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .filters import JobFilter
from django_filters.views import FilterView

from django.conf.urls import url


urlpatterns = [
    path('', views.main_view, name='main_view'),
    # 뉴스
    path('article', views.article_list, name='article_list'),
    path('article/dev/', views.article_dev_list, name='article_dev_list'),
    path('article/cloud/', views.article_cloud_list, name='article_cloud_list'),
    path('article/big_data/', views.article_big_data_list, name='article_big_data_list'),
    path('article/AI/', views.article_AI_list, name='article_AI_list'),
    path('article/IoT/', views.article_IoT_list, name='article_IoT_list'),
    path('article/devops/', views.article_devops_list, name='article_devops_list'),
    path('article/secure/', views.article_secure_list, name='article_secure_list'),
    path('article/new_tech/', views.article_new_tech_list, name='article_new_tech_list'),

    # 공모전
    path('contest', views.contest_list, name='contest_list'),
    path('contest/contest_game/', views.contest_game_list, name='contest_game_list'),
    path('contest/contest_science/', views.contest_science_list, name='contest_science_list'),
    path('contest/contest_job/', views.contest_job_list, name='contest_job_list'),
    

    #채용공고
    path('job/', views.job_list, name='job_list'),

    #채용공고 필터
    path('', FilterView.as_view(
            filterset_class=JobFilter,
            template_name='job/job_detail_list_temp.html'),
         name='index'),

    #트렌드
    path('trend/', views.trend, name='trend'),

    #로그인
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    #로그아웃
    path('accounts/logout/', auth_views.LogoutView.as_view(), {'next_page': None}, name='logout'),

    #회원가입
    path('register/', views.register, name = 'register'),

    #회원정보 수정
    path('update/', views.update,name='update'),

    #마이페이지
    path('mypage/', views.mypage, name = 'mypage'),

    #스터디 전체 리스트 페이지
    path('study/', views.study, name='study'),

    #내 스터디 페이지
    path('study/my', views.my_study, name='my_study'),

    #스터디 만들기
    path('study/create', views.create_study, name='create_study'),

    #스터디 join
    path('study/join/<id>', views.join_study, name='join_study'),

    #스터디 cancel
    path('study/cancel/<id>', views.cancel_study, name='cancel_study'),

]