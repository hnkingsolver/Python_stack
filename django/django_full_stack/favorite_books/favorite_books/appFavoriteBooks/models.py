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
    #posted_book is the related name - one to many - a user can upload many books, but a book can only be uploaded by one user 
    #favorited_book is manytomany related name - users can favorite many books, and many books can have many favorites
    
    
class BookManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['title']) < 1:
            errors['title_too_short'] = "Title is too short"
        # book_title = Book.objects.filter(book_title=requestPOST['book_title'])
        if len(requestPOST['desc']) < 5:
            errors['desc_too_short'] = "Description too short"
        return errors
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    users_who_like = models.ManyToManyField(User, related_name = "liked_book")
    uploaded_by = models.ForeignKey(User, related_name='posted_book', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()