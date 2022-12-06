from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

blog_posts = {'blog_post_1': 'blog post 1 loaded',
              'blog_post_2': 'blog post 2 loaded'}


def index(request):
    return render(request, 'blog/index.html', {'posts':blog_posts.keys})


def blog_post(request, post):
    #try:
        return render(request, 'blog/post.html', {
            'post_title':post,
            'post_content':blog_posts[post]
            })
    #except:
     #   return HttpResponseNotFound('<h1>this post does not exist</h1>')


def blog_post_by_index(request, post_index):
    try:
        post_key = list(blog_posts.keys())[post_index - 1]
        redirect_path = reverse('blog:entries', args = [post_key])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('<h1>this post does not exist</h1>')
    # Create your views here.
