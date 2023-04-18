from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Champion, Comment


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def contact(request):
    return render(request, "./contact-us.html")
