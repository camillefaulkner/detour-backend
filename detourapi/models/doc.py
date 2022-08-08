from django.db import models


class Doc(models.Model):

    publicURL = models.URLField()
    user = models.ForeignKey("DetourUser", on_delete=models.CASCADE, related_name="docs")
