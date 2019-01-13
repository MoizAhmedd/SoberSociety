from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Challenge(models.Model):
    author = models.ForeignKey(
            'auth.User',
            on_delete = models.CASCADE,
        )
    name = models.TextField()
    days = models.CharField(max_length = 5)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('challenges')

    def getint(self):
        return int(self.days)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.CharField(max_length = 20)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    user = models.ForeignKey(
    'auth.User', on_delete = models.CASCADE,
    )
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)
    post_text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog')

class Comment(models.Model):
    post = models.ForeignKey('Blog',on_delete = models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
