from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'champion',
            'position',
            'excerpt',
            'content',
        )


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'excerpt',
            'content',
        )
