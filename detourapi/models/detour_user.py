from django.db import models
from django.contrib.auth.models import User


class DetourUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    allergies = models.CharField(max_length=40)
    greenroom_requests = models.CharField(max_length=50)
    
    @property 
    def full_name (self):
        return self.user.first_name + " " + self.user.last_name