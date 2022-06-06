# Generated by Django 4.0.4 on 2022-05-23 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=25, verbose_name='Имя автора')),
                ('mail', models.CharField(max_length=100, verbose_name='Почта')),
                ('count', models.IntegerField(verbose_name='Количество голосов')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Categoties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название категории')),
                ('amount', models.IntegerField(verbose_name='Количество опросов в категории')),
                ('reviews', models.IntegerField(verbose_name='Оценка категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=25, verbose_name='Название опроса')),
                ('description', models.TextField(max_length=25, verbose_name='Тема опроса')),
                ('votes_for', models.IntegerField(verbose_name='Голосов за')),
                ('votes_against', models.IntegerField(verbose_name='Голосов против')),
                ('creator', models.CharField(max_length=30, verbose_name='Автор опроса')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='HistoricalQuiz',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=25, verbose_name='Название опроса')),
                ('description', models.TextField(max_length=25, verbose_name='Тема опроса')),
                ('votes_for', models.IntegerField(verbose_name='Голосов за')),
                ('votes_against', models.IntegerField(verbose_name='Голосов против')),
                ('creator', models.CharField(max_length=30, verbose_name='Автор опроса')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Опрос',
                'verbose_name_plural': 'historical Опросы',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoties',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название категории')),
                ('amount', models.IntegerField(verbose_name='Количество опросов в категории')),
                ('reviews', models.IntegerField(verbose_name='Оценка категории')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Категория',
                'verbose_name_plural': 'historical Категории',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAuthors',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('author_name', models.CharField(max_length=25, verbose_name='Имя автора')),
                ('mail', models.CharField(max_length=100, verbose_name='Почта')),
                ('count', models.IntegerField(verbose_name='Количество голосов')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Автор',
                'verbose_name_plural': 'historical Авторы',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
