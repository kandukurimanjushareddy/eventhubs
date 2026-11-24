from django.db import models


class EventStatus(models.TextChoices):
    SCHEDULED = "scheduled", "Scheduled"
    CANCELLED = "cancelled", "Cancelled"
    COMPLETED = "completed", "Completed"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=EventStatus.choices,
        default=EventStatus.SCHEDULED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_time"]

    def __str__(self):
        return f"{self.title} ({self.start_time:%Y-%m-%d})"
