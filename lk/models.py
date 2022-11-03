from django.db import models
from datetime import datetime


class lk(models.Model):
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата время создания')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT, verbose_name='Пользователь ЛК', related_name='Пользователь', null=True)

    def __str__(self):
        return f'{self.user} '

    class Meta:
        verbose_name = 'Личный кабинет'
        verbose_name_plural = 'Кабинеты пользователей'
        ordering = ['time_add']