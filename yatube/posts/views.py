from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group
from django.core.paginator import Paginator
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

POST_COUNT = 10
User = get_user_model()


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = (
        Post
        .objects
        .filter(group=group)
        .order_by('-pub_date')[:POST_COUNT]
    )
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj' : page_obj
    }
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    template = 'posts/profile.html'
    title = f'Профайл пользователя {username}'
    post_list = (
        Post
        .objects
        .select_related('author')
        .filter(author__username=username))
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'post_list': post_list,
        'page_obj': page_obj,
        'author': author,

    }

    return render(request, template, context)


def post_detail(request, post_id):
    post_list = get_object_or_404(Post, id=post_id)
    template = 'posts/post_detail.html'
    context = {
        'post_list': post_list,
        'author': Post.author
    }
    return render(request, template, context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.author = request.user
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', request.user)
        return render(request, 'posts/create_post.html', {'form': form})

    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post.id)
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm(instance=post)
    return render(request, 'posts/create_post.html', {'form': form})
