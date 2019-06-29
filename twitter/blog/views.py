from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_edit(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.save()
        return redirect('post_edit')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'posts': posts})