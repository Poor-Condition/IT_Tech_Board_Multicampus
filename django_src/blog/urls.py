from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_new_tech_list, name='article_new_tech_list'),
]
