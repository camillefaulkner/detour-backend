from django.db import models


class ShowDate(models.Model):

    user = models.ForeignKey("DetourUser", on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=30)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    essential_notes = models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    docs = models.ManyToManyField("Doc", through="DocAssignment", related_name="showdates_by_doc")

    def __str__(self):
        return self.venue + ' ' + f'{self.date}'
