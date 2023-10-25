#urls index
from django.urls import path
from . import views

urlpattern = [
    path('berita/', views.berita, name='berita'),
    path('isi/', views.isi, name='isi'),
    path('isi1/', views.isi1, name='isi1'),
]