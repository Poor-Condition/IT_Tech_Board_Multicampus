from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('article', views.article_list, name='article_list'),
    path('article/dev/', views.article_dev_list, name='article_dev_list'),
    path('article/cloud/', views.article_cloud_list, name='article_cloud_list'),
    path('article/new_tech/', views.article_new_tech_list, name='article_new_tech_list'),
    path('job/', views.job_list, name='job_list'),
    path('job/cloud', views.job_cloud_list, name='job_cloud_list'),
    path('job/python', views.job_python_list, name='job_python_list'),
    path('job/db', views.job_db_list, name='job_db_list'),
]
