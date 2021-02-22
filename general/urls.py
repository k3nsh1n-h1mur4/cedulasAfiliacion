from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/register/', views.registerUser_view, name='registerU'),
    path('main/register', views.register_view, name='register'),
    path('main/listar/', views.listar_view, name='listar'),
    path('main/edit/<int:id>', views.edit_view, name='edit'),
    path('pdf/', views.create_pdf, name='pdf'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)