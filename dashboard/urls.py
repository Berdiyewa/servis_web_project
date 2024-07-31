from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tables', views.tables, name='tables'),
    path('billing', views.billing, name='billing'),
    path('notifications', views.notifications, name='notifications'),
    path('profile', views.profile, name='profile'),
    path('base_sign', views.base_sign, name='base_sign'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]
