from typing import no_type_check

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.deletion import CASCADE

User = get_user_model()

class QuestionType(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False
        )

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопросов'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Survey(models.Model):
    name = models.CharField(
        verbose_name='Имя опроса',
        max_length=256,
        blank=False
    )
    date_start = models.DateField(
        verbose_name='Дата старта опроса',
        blank=False,
        auto_now_add=False
    )
    date_end = models.DateField(
        verbose_name='Дата окончания опроса',
        blank=False,
    )
    description = models.CharField(
        verbose_name='Описание опроса',
        max_length=256,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['date_start']


class Question(models.Model):
    text = models.CharField(
        verbose_name='Текст вопроса',
        max_length=256,
        blank=False
        )
    type = models.ForeignKey(QuestionType,
        verbose_name='Тип вопроса',
        on_delete=models.CASCADE,
        blank=False,
        )
    survey = models.ForeignKey(Survey,
        verbose_name='Опрос',
        on_delete=models.CASCADE,
        blank=False,
        )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['text']

    def __str__(self):
        return f'{self.text}'


class Answer(models.Model):
    question = models.ForeignKey(Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE,
        blank=False,
        )
    text = models.CharField(
        verbose_name='Текст ответа',
        max_length=256,
        )

    def __str__(self):
        return f'{self.text}'
       
    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'
        ordering = ['question']


class Result(models.Model):
    interviewee = (models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='id опрашиваемого')
        )
    answer = models.ForeignKey(Answer,
        verbose_name='Ответ',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )
    question = models.ForeignKey(Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE,
        blank=False,
        )
    survey = models.ForeignKey(Survey,
        verbose_name='Опрос',
        on_delete=models.CASCADE,
        blank=False,
        )
    your_answer = models.CharField(
        verbose_name='Свой ответ',
        max_length=256,
        blank=True,
        )

    def __str__(self):
        return f'{self.interviewee}'

    class Meta:
        verbose_name = 'Результат опроса'
        verbose_name_plural = 'Результаты опросов'
        ordering = ['interviewee']
        UniqueConstraint(
            fields=['interviewee', 'answer', 'question', 'survey'],
            name='unique_interviewee')
