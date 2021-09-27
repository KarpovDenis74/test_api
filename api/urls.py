from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ViewAnswer, ViewQuestion, ViewResult, ViewSurvey

app_name = 'api'
router = DefaultRouter()
router.register('question',
    ViewQuestion,
    basename='question') 
router.register('survey',
    ViewSurvey,
    basename='survey')
router.register('answer',
    ViewAnswer,
    basename='answer')
router.register('result',
    ViewResult,
    basename='result')

urlpatterns = [
    path('v1/', include(router.urls)),
]
