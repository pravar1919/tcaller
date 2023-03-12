from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100, null=True, blank=True)
    spam = models.BooleanField(default=False,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
