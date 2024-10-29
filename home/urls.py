from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.HomeView.as_view(), name='home_view')
]
