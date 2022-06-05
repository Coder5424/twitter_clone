from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='Hello', max_length=100)
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return f'Profile {self.user.username}'

    def following(self):
        users = Relationship.objects.filter(from_user=self.user).values_list('to_user', flat=True)
        return User.objects.filter(id__in=users)

    def followers(self):
        users = Relationship.objects.filter(to_user=self.user).values_list('from_user', flat=True)
        return User.objects.filter(id__in=users)


class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.content


class Relationship(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relationship')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_to')

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'