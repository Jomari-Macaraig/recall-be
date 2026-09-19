from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from apps.content.models import Lesson
from apps.content.api.serializers import LessonListSerializer, LessonSerializer


class LessonListAPIView(ListAPIView):
    """Lists active lessons.

    Read-only endpoint (GET only) — returns every ``Lesson`` where
    ``is_active`` is True, serialized via ``LessonSerializer``.
    """

    queryset = Lesson.objects.filter(is_active=True)
    serializer_class = LessonListSerializer
    filter_backends = [SearchFilter]
    search_fields = ("title",)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.filter(is_active=True)
    serializer_class = LessonSerializer
