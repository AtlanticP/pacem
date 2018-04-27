from django.urls import path

from lists import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:file_name>/', views.list_articles, name='list_articles'),
    path('do/', views.create_article, name='do'),
]
