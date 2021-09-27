import datetime

from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.permissions import (AllowAny, IsAdminUser,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import GenericViewSet

from api.models import Answer, Question, QuestionType, Result, Survey
from api.serializers import (AnswerSerializer, QuestionSerializer,
                             QuestionTypeSerializer, ResultSerializer,
                             SurveySerializer)


class ViewQuestionType(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, ]
    serializer_class = QuestionTypeSerializer


class ViewSurvey(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = SurveySerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        now_date = datetime.date.today()
        queryset = Survey.objects.filter(data_start__lte=now_date,
                                   data_end__gte=now_date)
        return queryset


class ViewQuestion(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('survey', )


class ViewAnswer(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = AnswerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('question', )


class ViewResult(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = ResultSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('interviewee', )
