from dataclasses import fields
from .models import Quiz, Authors, Categoties
from django.forms import ModelForm, NumberInput, TextInput, Textarea

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_name','description','votes_for','votes_against','creator']

        widgets = {
            'quiz_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название опроса'
            }),
             'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
                'votes_for': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Голосов за'
            }),
                'votes_against': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Голосов против'
            }),
               'creator': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            })
        }


class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = ['author_name','mail','count']

        widgets = {
            'author_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя автора'
            }),
             'count': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количесвто созданных опросов'
            }),
                'mail': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            })
        }

class CategotiesForm(ModelForm):
    class Meta:
        model = Categoties
        fields = ['name','amount','reviews']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название категории'
            }),
             'amount': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество опросов данной категории'
            }),
                'reviews': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка категории'
            })
        }