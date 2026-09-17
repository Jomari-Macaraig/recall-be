from rest_framework import serializers
from apps.content.models import Lesson


class LessonListSerializer(serializers.ModelSerializer):
    """Serializes a ``Lesson`` for the API — title, content, and its
    section/subsection.
    """

    section = serializers.SlugRelatedField(slug_field="name", read_only=True)
    subsection = serializers.SlugRelatedField(
        slug_field="name", read_only=True
    )

    class Meta:
        model = Lesson
        fields = ("id", "title", "section", "subsection")


class LessonSerializer(serializers.ModelSerializer):
    """Serializes a ``Lesson`` for the API — title, content, and its
    section/subsection.
    """

    section = serializers.SlugRelatedField(slug_field="name", read_only=True)
    subsection = serializers.SlugRelatedField(
        slug_field="name", read_only=True
    )

    class Meta:
        model = Lesson
        fields = ("id", "title", "content", "section", "subsection")
