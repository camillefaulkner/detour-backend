from django.db import models


class GuestRequest(models.Model):

    user = models.ForeignKey("DetourUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    quantity = models.IntegerField()
    show_date = models.ForeignKey("ShowDate", on_delete=models.CASCADE, related_name="guest_requests")
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="guest_requests")
