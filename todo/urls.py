from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('current/', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodos, name='createtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('completed/', views.completed, name='completed'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
]