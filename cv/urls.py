from django.urls import path

from cv import views

urlpatterns = [
    path('', views.index, name='index'),
]

