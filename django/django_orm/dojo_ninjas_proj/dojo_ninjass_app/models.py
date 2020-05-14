from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ninjas = a list of ninjas associated with a given dojo

class Ninja(models.Model):
    dojo_id = models.IntegerField()
    frist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    home = models.ForeignKey(Dojo, related_name = "ninjas", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)