from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("contact", views.ContactUs.as_view(), name="contact"),
    path("<slug:slug>", views.UserPost.as_view(), name="user-post"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
]
