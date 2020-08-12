from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('article/', views.article_new_tech_list, name='article_new_tech_list'),
]
