from django.contrib import admin
from .models import Post, Champion, Comment

# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Champion)
class PostAdmin(admin.ModelAdmin):

    list_display = ('champion_name', 'primary_role')
    search_fields = ['champion_name', 'primary_role']
    list_filter = ('primary_role', 'champion_name')
    prepopulated_fields = {'slug': ('title',),
                           'champion_name': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
