from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.content.models import Lesson
from apps.content.api.serializers import LessonSerializer


class LessonListAPIView(ListAPIView):
    """Lists active lessons.

    Read-only endpoint (GET only) — returns every ``Lesson`` where
    ``is_active`` is True, serialized via ``LessonSerializer``.
    """

    queryset = Lesson.objects.filter(is_active=True)
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.filter(is_active=True)
    serializer_class = LessonSerializer
