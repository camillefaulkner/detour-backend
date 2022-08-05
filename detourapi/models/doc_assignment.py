from django.db import models


class DocAssignment(models.Model):

    doc = models.ForeignKey("Doc", on_delete=models.CASCADE)
    show_date = models.ForeignKey("ShowDate", on_delete=models.CASCADE)