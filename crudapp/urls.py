from django.contrib import admin
from django.urls import path
from crudapp.views import*
from crudapp import views

urlpatterns =[

#     path('',views.book_list, name='book_list'),
#     path('create/', views.create_task, name='create_task'),
#     path('detail/<slug:slug>/',views.book_detail, name='book_detail'),
#     path('update/<slug:slug>/', views.book_update, name='book_update'),
#     path('delete/<slug:slug>/', views.book_delete, name='book_delete'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('book/<slug:slug>/', views.book_detail, name='book_detail'),



 ]