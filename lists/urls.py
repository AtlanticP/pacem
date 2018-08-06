from django.urls import path

from lists import views
  
urlpatterns = [
    path('', views.index, name='index'),
    path('do/', views.create_article, name='do'),
    path('contacts/', views.contacts, name='contacts'),
    path('jQuery/', views.jQuery_index),
    path('jQuery/<int:item_id>/', views.jQuery_view, name='jQuery_view'),
    path('<str:lst_name>/', views.list_lan, name='list_lan'),
    path('<str:lst_name>/<int:item_id>/', views.code_page, name='code_page'),
]
