from django.db import models
from django.contrib.auth.models import User

class Applicant(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.user.first_name

