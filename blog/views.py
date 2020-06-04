from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from blog.forms import PostForm
from blog.models import Post


def blog(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/post_details.html', context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:blog'))
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/add_post.html', context)


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            # post.slug = slugify(post.title)
            # post.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'blog/edit_post.html', context)
