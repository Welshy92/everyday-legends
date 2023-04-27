from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Champion, Comment
from .forms import CommentForm, PostForm, EditForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ChampList(generic.ListView):
    model = Champion
    queryset = Champion.objects.order_by('champion_name')
    template_name = 'champions.html'


class UserPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "user-post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "user-post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
            )


class NewPost(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "./create-post.html",
            {"post_form": PostForm()},
            )

    def post(self, request, *args, **kwargs):

        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.instance.status = 1
            postit = post_form.save()

            return HttpResponseRedirect(reverse('index'))
        else:

            post_form = PostForm()

        return render(
            request,
            "./post-error.html",
            {"post_form": PostForm()},
            )


class EditPost(View):

    def get(self, request, slug, *args, **kwargs):

        post = get_object_or_404(Post, slug=slug)
        edit_form = EditForm(instance=post)
        context = {
            'edit_form': edit_form
        }

        return render(
            request,
            "./edit-post.html",
            context,
            )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        post.excerpt = request.POST['excerpt']
        post.content = request.POST['content']
        post.save()
        return HttpResponseRedirect(reverse('index'))


class DeletePost(View):

    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Post, slug=slug)
        item.delete()
        return HttpResponseRedirect(reverse('index'))


class ContactUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "./contact-us.html")


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('user-post', args=[slug]))
