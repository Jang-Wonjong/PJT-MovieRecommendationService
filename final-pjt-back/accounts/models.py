from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here
class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    image = ProcessedImageField(
        blank=True,
        upload_to='profile_images/%Y/%m/%d/',
        processors=[ResizeToFill(200,200)],
        format='JPEG',
        options={'quality': 100}
        )
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')