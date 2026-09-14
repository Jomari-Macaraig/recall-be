from django.contrib import admin

from apps.content.models import Lesson, Section, SubSection


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "section",
        "subsection",
        "is_public",
        "is_published",
        "user",
        "is_active",
    )

    list_filter = ("section", "subsection", "is_active")
    list_editable = ("is_public", "is_published", "is_active")
    search_fields = ("title",)


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Section)
admin.site.register(SubSection)
