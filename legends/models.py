from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

POSITION_CHOICES = [
    ("TOP", "Top Lane"),
    ("JNG", "Jungler"),
    ("MID", "Mid Lane"),
    ("ADC", "Marksman"),
    ("SUP", "Support"),
]


class Champion(models.Model):
    title = models.CharField(max_length=100, unique=True, default='champ name')
    champion_name = models.CharField(max_length=100, unique=True, default='champ')
    primary_role = models.CharField(max_length=3, choices=POSITION_CHOICES)
    slug = models.SlugField(max_length=100, unique=True, default='slug')


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="legends_posts"
    )
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    champion = models.ManyToManyField(Champion)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=200, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='legends_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
