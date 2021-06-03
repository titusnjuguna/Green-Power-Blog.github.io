from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to="images")
    summary = models.TextField(max_length=150,blank=True)
    content= RichTextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def save(self):
        super().save()
        img = Image.open(self.header_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (800,400)
            img.thumbnail(output_size)
            img.save(self.header_image.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})    