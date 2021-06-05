"""diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, re_path, include
from diploma_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('portfolio/pupil/', views.pupil_page, name='pupil'),
    path('portfolio/pupil/add_diploma', views.add_diploma, name='add_diploma'),
    path('portfolio/teacher/', views.teacher_page, name='teacher'),
    path('portfolio/login_page/', views.login_page, name='login_page'),
    path('portfolio/logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^show_grade$', views.show_grade, name='show_grade'),
    url(r'^show_nomin$', views.show_nomin, name='show_nomin'),
    url(r'^delete_diplomas$', views.delete_diplomas, name='delete_diplomas'),
    #url(r'^show_portfolio_teach$', views.show_portfolio_teach, name='show_portfolio_teach'),
    url(r'create_report$', views.create_report, name='create_report'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('portfolio/base/', views.base, name='base'),

]
