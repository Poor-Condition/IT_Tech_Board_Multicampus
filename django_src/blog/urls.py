from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('article', views.article_list, name='article_list'),
    path('article/article_dev/', views.article_dev_list, name='article_dev_list'),
    path('article/article_cloud/', views.article_cloud_list, name='article_cloud_list'),
    path('article/article_new_tech/', views.article_new_tech_list, name='article_new_tech_list')
]
