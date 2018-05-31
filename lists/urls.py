from django.urls import path

from lists import views
  
urlpatterns = [

    # path('python/<int:item_id>/', views.code_page, name='code_page'),
    path('<str:lst_name>/<int:item_id>/', views.code_page, name='code_page'),
    path('python/', views.list_lan, name='list_lan'),
    path('do/', views.create_article, name='do'),
    path('', views.index, name='index'),
]
