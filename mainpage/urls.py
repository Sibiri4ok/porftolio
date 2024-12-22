from mainpage import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('auth/complete/google-oauth2/', views.login_error, name='google_login_error'),
]