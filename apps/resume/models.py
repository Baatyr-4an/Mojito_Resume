from django.conf import settings
from django.db import models
from django.db.models.fields.related import OneToOneField
from apps.users.models import Profile
from apps.users.models import User

class Resume(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    midlename = models.CharField(max_length=100, verbose_name='Отчество')
    citizenship = models.CharField(max_length=100, verbose_name='Гражданство')
    nationality = models.CharField(max_length=100, verbose_name='Национальнось', )
    wish_post = models.CharField(max_length=120, verbose_name='Желаемая должность')
    about_yourself = models.TextField(blank=True, null=True)
    accounts = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=200, verbose_name='E-mail')
    contacts = models.CharField(max_length=10, verbose_name='Номер')
    
    def finished(self):
        self.save()

class ResumeImage(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE, 
        related_name='resume_image'
    )
    image = models.ImageField(
        upload_to='resume',
        verbose_name='Картинки'
    )

    def __str__(self):
        return f"{self.resume.id}"