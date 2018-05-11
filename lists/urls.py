from django.urls import path

from lists import views

urlpatterns = [
    path('', views.index, name='index'),
    path('do/', views.create_article, name='do'),
]
