from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex=r'^\+996\d{9}$', message='Номер телефона необходимо написать в формате: "+996*********".')

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        validators = [phone_validator],
        max_length=15,
        verbose_name='Номер телефона'
    )
    user_age = models.IntegerField(
        verbose_name='Возраст',
        null=True, blank=True
    )
    birthday = models.DateField(
        null=True, blank=True
    )

    def __str__(self):
        return self.username
    
    @property 
    def age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year
            if today.month < self.birthday.month or (today.month == self.birthday.month and today.day < self.birthday.day):
                age -= 1
                self.user_age = age
                self.save()
                return age
            return None    
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
