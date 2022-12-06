from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:post_index>', views.blog_post_by_index, name='entries_index'),
    path('<str:post>', views.blog_post, name='entries')    
]
