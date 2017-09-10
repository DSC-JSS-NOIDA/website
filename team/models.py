from django.db import models
from django.conf import settings
from django.contrib import auth


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Team(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='media/team/',
                            null=True, blank=True, height_field="height_field",
                            width_field="width_field")
    height_field = models.IntegerField(default=0,blank=True)
    width_field = models.IntegerField(default=0,blank=True)
    github_link = models.URLField(max_length=50)
    email = models.EmailField(max_length=250)
    linkedin = models.URLField(
        max_length=250)
    description = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name
