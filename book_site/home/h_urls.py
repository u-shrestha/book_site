from . import views
from django.urls import path

urlpatterns = [
    path('', views.f_home, name='home_page'),
    path('<btitle>/', views.f_detail, name='detail_page'),

   ]
