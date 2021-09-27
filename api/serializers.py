from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.models import Answer, Question, QuestionType, Result, Survey

User = get_user_model()


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'name', )
        model = QuestionType


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'name', 'date_start', 'date_end', 'description',)
        model = Survey


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'text', 'type', 'survey', )
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'question', 'text', )
        model = Answer


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'interviewee',
            'answer',
            'question',
            'survey', 
            'your_answer', )
        model = Result
