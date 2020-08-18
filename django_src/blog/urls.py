from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('article', views.article_list, name='article_list'),
    path('article/dev/', views.article_dev_list, name='article_dev_list'),
    path('article/cloud/', views.article_cloud_list, name='article_cloud_list'),
    path('article/new_tech/', views.article_new_tech_list, name='article_new_tech_list'),

    # 공모전
    path('', views.main_view, name='main_view'),
    path('contest', views.contest_list, name='contest_list'),
    path('contest/contest_game/', views.contest_game_list, name='contest_game_list'),
    path('contest/contest_science/', views.contest_science_list, name='contest_science_list'),
    path('contest/contest_job/', views.contest_job_list, name='contest_job_list'),

    path('job/', views.job_list, name='job_list'),
    path('job/cloud', views.job_cloud_list, name='job_cloud_list'),
    path('job/python', views.job_python_list, name='job_python_list'),
    path('job/db', views.job_db_list, name='job_db_list'),

    #로그인
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    #로그아웃
    path('accounts/logout/', auth_views.LogoutView.as_view(), {'next_page': None}, name='logout'),

    #회원가입
    path('register/', views.register, name = 'register'),
]
