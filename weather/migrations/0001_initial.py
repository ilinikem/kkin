# Generated by Django 5.0.1 on 2024-01-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(help_text='Введите название города', max_length=30, unique=True, verbose_name='Название города')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Создается автоматически. Дата и время создания записи', verbose_name='Дата и время создание записи')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Обновляется автоматически. Дата и время обновления записи', verbose_name='Дата и время обновления записи')),
                ('temperature', models.DecimalField(blank=True, decimal_places=2, help_text='Текущая температура в градусах Цельсия', max_digits=5, null=True, verbose_name='Температура')),
                ('pressure', models.DecimalField(blank=True, decimal_places=2, help_text='Атмосферное давление в мм рт. ст.', max_digits=6, null=True, verbose_name='Давление')),
                ('wind_speed', models.DecimalField(blank=True, decimal_places=2, help_text='Скорость ветра в м/с', max_digits=5, null=True, verbose_name='Скорость ветра')),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погода в городах',
            },
        ),
    ]
