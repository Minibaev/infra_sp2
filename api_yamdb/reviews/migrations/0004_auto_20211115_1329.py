# Generated by Django 2.2.16 on 2021-11-15 08:29

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20211113_1221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['pub_date'], 'verbose_name': 'Рецензия', 'verbose_name_plural': 'Рецензии'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.validators.year_validator], verbose_name='Год'),
        ),
    ]