# Generated by Django 4.1.3 on 2022-11-03 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_fio_user_name_user_patronymic_user_surname_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]