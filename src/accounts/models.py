from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    registration_ip = models.GenericIPAddressField(protocol="both")

    def getIpAddress(self):
        return "Hello, my name is {}".format(self.first_name)
