from django.urls import path
from . import views

app_name = 'authApp'

urlpatterns = [
    path('registration/', views.userReg, name='userReg'),
    path('', views.userLogin, name='userLogin'),
    path('logout/', views.userLogout, name='userLogout'),
]