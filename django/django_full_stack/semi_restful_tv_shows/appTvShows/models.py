from django.db import models
import re

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print(postData)
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = 'Network needs to be at least 3 characters'
        if len(postData['release_date']) < 10:
            errors['release_date'] = "Complete the release date field"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description needs to be at least 10 characters"
        return errors
        
        
        
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()