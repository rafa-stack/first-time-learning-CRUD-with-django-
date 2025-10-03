from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('berita/<int:id>/', views.detail, name='detail'),
    path('tambah/', views.tambah_berita, name='tambah_berita'),
    path('hapus/<int:id>/', views.hapus_berita, name='hapus_berita'),
    path('login/', auth_views.LoginView.as_view(template_name='crudapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('hapus-akun/', views.hapus_akun, name='hapus_akun'),
]