from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self,requestPOST):
        errors = {}
        if len(requestPOST['first_name']) < 3:
            errors['first_name'] = "First name is too short."
        FNAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
        if len(requestPOST['first_name']) > 0:
            if not FNAME_REGEX.match(requestPOST['first_name']):
                errors['first_name_format'] = "First name may not have speacial characters"
        if len(requestPOST['last_name']) < 3:
            errors['last_name'] = "Last name is too short"
        LNAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
        if len(requestPOST['last_name']) > 0:
            if not FNAME_REGEX.match(requestPOST['last_name']):
                errors['last_name_format'] = "Last name may not have speacial characters"
        if len(requestPOST['email']) < 5:
            errors['email'] = "Email is too short"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(requestPOST['email']) > 0:
            if not EMAIL_REGEX.match(requestPOST['email']):
                errors['email_format'] = "Email is not in correct format"
        users_with_email = User.objects.filter(email=requestPOST['email'])
        if len(users_with_email) > 0:
            errors['dup_email'] = "Email already in use"
        if len(requestPOST['password']) <8:
            errors['password'] = "Password is too short"
        if requestPOST['password'] != requestPOST['password_conf']:
            errors['no_match'] = "Passswords must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class GroupManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['name']) == 0:
            errors['no_empty_entry'] = "Must be completed"
        if len(requestPOST['desc']) == 0:
            errors['no_empty_entry'] = "Must be completed"
        if len(requestPOST['name']) < 5:
            errors['author_too_short'] = "Group name is too short"
        if len(requestPOST['desc']) < 10:
            errors['quote_too_short'] = "Description is too short"
        return errors

class Group(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    added_by = models.ForeignKey(User, related_name='added_group', on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name='joined_group')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GroupManager()