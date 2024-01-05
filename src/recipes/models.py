from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField() #cooking time in mins
    ingredients = models.CharField(max_length=350)
    description = models.TextField(max_length=120)
    
    def __str__(self):
        return self.name
