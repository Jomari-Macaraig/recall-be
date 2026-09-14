"""URL routes for the ``content`` app's API (mounted under /api/content/ in config.urls)."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.content.api.views import LessonListAPIView, LessonRetrieveAPIView

urlpatterns = [
    path("lesson", LessonListAPIView.as_view()),
    path("lesson/<int:pk>", LessonRetrieveAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
