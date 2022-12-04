from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_index>', views.blog_post_by_index, name='entries_index'),
    path('<str:post>', views.blog_post, name='entries')    
]
