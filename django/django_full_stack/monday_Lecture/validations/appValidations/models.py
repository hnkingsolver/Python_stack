from django.db import models
import re


class PhillipManager(models.Manager):
    def create_validator(self, requestPOST):
        errors = {}
        if len(requestPOST ['name']) < 3:
            errors['name'] = "Name is too short"
        if len(requestPOST['model_no']) < 3:
            errors ['model_no'] = "Model Number is too short"
        if len(requestPOST['email']) < 5:
            errors['email'] = "Email too short"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
        if len(requestPOST['email']) > 0:
            if not EMAIL_REGEX.match(requestPOST['email']):
                errors['email_format'] = "Email is not in correct format"
        if len(requestPOST['name']) > 0:
            if not NAME_REGEX.match(requestPOST['name']):
                errors['name_format'] = "Name not in format"
        phillips_with_email = Phillip.objects.filter(email=requestPOST['email'])
        if len(phillips_with_email) > 0:
            errors['dup_email'] = "Email already in database"
        return errors

class Phillip(models.Model):
    name = models.TextField()
    model_no = models.IntegerField()
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = PhillipManager()