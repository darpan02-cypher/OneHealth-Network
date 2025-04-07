from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('chgpwdpage/', views.changePwdPage, name='changepwdpage'),
    path('newuser/', views.newUser, name='newuser'),
    path('login/', views.login, name="verify"),
    path('createuser/', views.createUser, name="createuser"),
    path('changepwd/', views.changePwd, name="changepwd"),
    path('logoff/', views.logoff, name="logoff"),
]