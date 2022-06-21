# URL adresy 
from django.urls import path
from . import views

app_name = 'learn'

urlpatterns = [
    path('', views.index, name="index"),# Zakladna stranka
    path('mode', views.mode, name="mode"),
    path('register/', views.register, name="register"), # Stranka pre registraciu 
    path('check/', views.check, name='check'), # Stranka pre kontrolu
    path('add/', views.add, name='add'), # Stranka na pridavanie a zobrazovanie slovicok
    path('detail/word/<int:word_id>/', views.detail, name = "detail" ), # Detailny nahlad podstatnych a pridavnych mien
    path('detail/werb/<int:werb_id>/', views.detail, name = "detail" ), # Detailny nahlad slovies
    path('add/delete/word/<int:word_id>/', views.delete , name = "delete"), # Vymazanie slovicok
    path('add/delete/werb/<int:werb_id>/', views.delete , name = "delete"), # Vymazanie slovies
    path('detail/werb/<int:werb_id>/change/', views.change , name = "change"), # Zmenenie slovicok
    path('detail/word/<int:word_id>/change/', views.change , name = "change"), # Zmenenie slovies
]