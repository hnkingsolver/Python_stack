from django.db import models

# ONE Dungeon has many prisoners
# ONE Prisoner has ONE Dungeon
# ONE TO MANY


# ONE Dungeons has MANY dislikes
# ONE PRISONER has MANY dislikes
# MANY TO MNAY 


class Dungeon(models.Model):
    name = models.TextField()
    num_people_inside = models.IntegerField()
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    
class Prisoner(models.Model):
    first_name = models.TextField()
    last_name =models.TextField(null=True)
    dungeon = models.ForeignKey(Dungeon,related_name="all_prisoners", on_delete=models.CASCADE)
    dungeons_disliked= models.ManyToManyField(Dungeon, related_name= 'prisoners_that_dislike') # name of the class up there ^^^ is what we want is these parenthesis
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    