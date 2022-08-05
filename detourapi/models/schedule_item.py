from django.db import models


class ScheduleItem(models.Model):

    time = models.TimeField()
    description = models.CharField(max_length=40)
    show_date = models.ForeignKey("ShowDate", on_delete=models.CASCADE, related_name="schedule_items")
    user = models.ForeignKey("DetourUser", on_delete=models.CASCADE)