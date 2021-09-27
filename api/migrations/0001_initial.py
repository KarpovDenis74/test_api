# Generated by Django 2.2.10 on 2021-09-26 22:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='Текст ответа')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
                'ordering': ['question'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Тип вопроса',
                'verbose_name_plural': 'Типы вопросов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя опроса')),
                ('date_start', models.DateField(verbose_name='Дата старта опроса')),
                ('date_end', models.DateField(verbose_name='Дата окончания опроса')),
                ('description', models.CharField(max_length=256, verbose_name='Описание опроса')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
                'ordering': ['date_start'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviewee', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='id опрашиваемого')),
                ('your_answer', models.CharField(max_length=256, verbose_name='Свой ответ')),
                ('answer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Answer', verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question', verbose_name='Вопрос')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Survey', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Результат опроса',
                'verbose_name_plural': 'Результаты опросов',
                'ordering': ['interviewee'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Survey', verbose_name='Опрос'),
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.QuestionType', verbose_name='Тип вопроса'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Question', verbose_name='Вопрос'),
        ),
    ]