from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __repr__(self):
    #     contents = {
    #         "db" : User.objects.all()
    #     }
    #     return "contents.format.self
    # "First_name: {}".format(self.first_name), "last_name {}".format(self.last_name), "email_address {}".format(self.email_address), "age{}".format(self.age)
    #idk... need to ask about this^^^