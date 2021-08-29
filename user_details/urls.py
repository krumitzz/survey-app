from django.urls import path

from .views import (
    UserSurveyView,
)

app_name = 'user_details'
urlpatterns = [
    path('', UserSurveyView.as_view(), name='user_survey'),
]