from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Article title', help_text='Max. length 50 symbols', unique=True)
    text = models.TextField(verbose_name='Article content', help_text='Input here article content')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(verbose_name='Draft', default=False)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    


    def __str__(self):
        return f'{self.title}'


class Social_medial(models.Model):
    SOCIAL_MEDIA_CHOICE = (
        ('instagram', 'Instagram'),
        ('facebook-f', 'Facebook'),
        ('twitter', 'Twitter'),
        ('vk', 'VKontakte'),
        ('pinterest', 'Pinterest'),
        ('whatsapp', 'WhatsApp'),
        ('youtube', 'YouTube'),
        ('google', 'Google'),
    )
    name = models.CharField(max_length=30, verbose_name='Social media', choices=SOCIAL_MEDIA_CHOICE)
    url = models.URLField(unique=True, verbose_name='Social media url')
    
    def __str__(self):
        return f'{self.name}'
    
class SliderImage(models.Model):
    img = models.ImageField(verbose_name='image', upload_to='media/%Y/%m/%d')
    video = models.FileField(verbose_name='video', upload_to='media/%Y/%m/%d')
    
    def __str__(self) -> str:
        return 'img'

class AboutMe(models.Model):
    text1 = models.TextField()
    