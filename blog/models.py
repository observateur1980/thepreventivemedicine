from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

User = get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    # comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    


