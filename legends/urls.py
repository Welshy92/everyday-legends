from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("index", views.PostList.as_view(), name="index"),
    path("contact", views.ContactUs.as_view(), name="contact"),
    path("champions", views.ChampList.as_view(), name="champions"),
    path("post", views.NewPost.as_view(), name="new_post"),
    path("edit/<slug:slug>", views.EditPost.as_view(), name="edit_post"),
    path("delete/<slug:slug>", views.DeletePost.as_view(), name="delete_post"),
    path("<slug:slug>", views.UserPost.as_view(), name="user_post"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
]
