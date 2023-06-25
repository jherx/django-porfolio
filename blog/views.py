from django.shortcuts import render, get_object_or_404
from .models import Post

def render_post(req):
    post = Post.objects.all()
    return render(req, 'post.html', {'post': post})

def post_detail(req,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(req, 'post_detail.html', {"post":post})