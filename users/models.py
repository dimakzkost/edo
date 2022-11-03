from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=False, editable=False, verbose_name='Логин', unique=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    surname = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    FIO = models.CharField(max_length=100, blank=True, verbose_name='ФИО')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

