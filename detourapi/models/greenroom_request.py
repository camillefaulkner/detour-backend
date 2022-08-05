from django.db import models


class GreenRoomRequest(models.Model):

    request = models.CharField(max_length=40)
    user = models.ForeignKey("DetourUser", on_delete=models.CASCADE)
    show_date = models.ForeignKey("ShowDate", on_delete=models.CASCADE, related_name="gr_requests")
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="gr_requests")