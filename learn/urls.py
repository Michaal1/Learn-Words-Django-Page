from django.urls import path
from . import views

app_name = 'learn'

urlpatterns = [
    path('', views.index, name="index"),
    path('mode', views.mode, name="mode"),
    path('register/', views.register, name="register"),
    path('check/', views.check, name='check'),
    path('add/', views.add, name='add'),
    path('detail/word/<int:word_id>/', views.detail, name = "detail" ),
    path('detail/werb/<int:werb_id>/', views.detail, name = "detail" ),
    path('add/delete/word/<int:word_id>/', views.delete , name = "delete"),
    path('add/delete/werb/<int:werb_id>/', views.delete , name = "delete"),
    path('detail/werb/<int:werb_id>/change/', views.change , name = "change"),
    path('detail/word/<int:word_id>/change/', views.change , name = "change"),
]