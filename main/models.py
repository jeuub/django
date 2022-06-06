from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

def validate_even(value):
    if (value <=0) | (value >10):
        raise ValidationError(
            _('%(value)s. Поле должно быть больше 0 и меньше или равно 10 '),
            params={'value': value},
        )


class Categoties(models.Model):
    name = models.CharField('Название категории', max_length=25)
    amount = models.IntegerField('Количество опросов в категории')
    reviews = models.IntegerField('Оценка категории', validators=[validate_even])

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Authors(models.Model):
    author_name = models.CharField('Имя автора', max_length=25)
    mail = models.CharField('Почта', max_length=100)
    count = models.IntegerField('Количество опросов')

    history = HistoricalRecords()

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Quiz(models.Model):
    quiz_name = models.CharField('Название опроса', max_length=25)
    description = models.TextField('Описание опроса')
    category = models.ManyToManyField(Categoties, verbose_name='Категория')
    votes_for = models.IntegerField('Голосов за')
    votes_against = models.IntegerField('Голосов против')
    creator = models.ManyToManyField(Authors, verbose_name='Автор')

    history = HistoricalRecords()

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

