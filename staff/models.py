from django.db import models
from users.models import User


class Staff(models.Model):
    OFFICE = 'OF'
    APTEKA = 'APT'
    OF_AP = [(OFFICE, 'Офис'), (APTEKA, 'Аптека'),]
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    surname = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    FIO = models.CharField(max_length=100, blank=True, verbose_name='ФИО')
    FIO_otkogo = models.CharField(max_length=100, blank=True, verbose_name='ФИО от кого')
    FIO_komy = models.CharField(max_length=100, blank=True, verbose_name='ФИО кому')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT, verbose_name='Пользователь', related_name='user', null=True)
    office_apteka = models.CharField(max_length=10, choices=OF_AP, default=OFFICE, verbose_name='Офис или аптека')
    job_title = models.ForeignKey('JobTitle', on_delete=models.PROTECT, verbose_name='Должность', related_name='JobTitle', null=True)
    sub_division = models.ForeignKey('SubDivision', on_delete=models.PROTECT, verbose_name='Подразделение', related_name='SubDivision', null=True)


    def __str__(self):
        return f'{self.FIO} '

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['FIO']


class JobTitle(models.Model):
    name = models.CharField(verbose_name='Должность', max_length=250, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class SubDivision(models.Model):
    name = models.CharField(verbose_name='Подразделение', max_length=250, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
