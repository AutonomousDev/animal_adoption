from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from animals.models import Animal


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    animal = models.ForeignKey(Animal, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])