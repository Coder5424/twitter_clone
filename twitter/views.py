from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post, Profile, Relationship
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm


@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {'posts': posts, 'form': form}
    return render(request, 'twitter/newsfeed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'twitter/register.html', context)


@login_required
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'twitter/profile.html', context)


@login_required
def editor(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'twitter/editor.html', context)


@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    rel = Relationship(from_user=current_user, to_user=to_user)
    rel.save()
    return redirect('home')


@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    rel = Relationship.objects.get(from_user=current_user, to_user=to_user)
    rel.delete()
    return redirect('home')


@login_required
def search(request):
    username = request.GET.get('search2')
    users = User.objects.filter(username__contains=username)
    context = {'users': users}
    return render(request, 'twitter/search.html', context)




