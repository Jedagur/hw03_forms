from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group
from django.core.paginator import Paginator
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from yatube.settings import POST_COUNT, ON_PAGE
from django.contrib.auth.decorators import login_required

User = get_user_model()


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, ON_PAGE)
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
    )
    paginator = Paginator(posts, ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj
    }
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    template = 'posts/profile.html'
    post_list = author.posts.select_related('author')
    paginator = Paginator(post_list, ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'page_obj': page_obj,
        'author': author,

    }

    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    template = 'posts/post_detail.html'
    context = {
        'post': post
    }
    return render(request, template, context)


@login_required
def post_create(request):
    is_edit = False
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', request.user)
        return render(request, 'posts/create_post.html', {'form': form})

    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    is_edit = True
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post.id)
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm(instance=post)
    return render(request, 'posts/create_post.html', {'form': form})
