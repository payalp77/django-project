from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('all_members/',views.all_members,name='all_members'),
    path('contacts/', views.contacts,name='contacts'),
    path('add_newmembers/', views.add_newmembers,name='add_newmembers'),
    path('all_members/detail/update/<int:id>', views.update, name='update'),
     path('all_members/detail/delete/<int:id>', views.delete, name='delete'),
    path('all_members/detail/<int:id>',views.detail, name='detail'),  
]