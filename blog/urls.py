from django.urls import path

from blog import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('add-post/', views.add_post, name='add-post'),
    path('<slug:slug>/', views.post_details, name='post-details'),
    path('<slug:slug>/edit/', views.edit_post, name='edit-post'),

]
