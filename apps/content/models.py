from django.db import models

from apps.base.models import Audit, UserAudit


class Section(Audit):
    """Top-level grouping of curriculum content (e.g. a subject or module).

    Sections are the root of the content hierarchy: each ``SubSection`` and
    ``Lesson`` belongs to exactly one ``Section``.
    """

    name = models.CharField(max_length=32)

    def __str__(self):
        """Human-readable representation."""
        return self.name

    def __repr__(self):
        """Unambiguous developer representation."""
        return self.name


class SubSection(Audit):
    """A subdivision within a ``Section``, used to further group lessons.

    Optional in the hierarchy — a ``Lesson`` may belong to a section directly
    without a subsection (see ``Lesson.subsection``).
    """

    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        """Human-readable representation."""
        return self.name

    def __repr__(self):
        """Unambiguous developer representation."""
        return self.name


class Lesson(UserAudit):
    """A single unit of learning content.

    Always belongs to a ``Section`` and optionally to one of that section's
    ``SubSection``s. Visibility is controlled independently by two flags:
    ``is_public`` (whether it's visible outside the owning account/org) and
    ``is_published`` (whether it's finished and ready to be shown at all).
    """

    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subsection = models.ForeignKey(
        SubSection, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=32)
    content = models.TextField()
    is_public = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        """Human-readable representation."""
        return self.title

    def __repr__(self):
        """Unambiguous developer representation."""
        return self.title
