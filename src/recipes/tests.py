from django.test import TestCase
from .models import Recipe                   #to access Recipe model
# Create your tests here.

class RecipeModelTest(TestCase):
    #this is the test example
    def setUp(self):
        Recipe.objects.create(
            recipe_id =1,
            name = 'Test recipe',
            cooking_time = 15,
            ingredients = 'ingredient 1, ingredient 2',
            description = 'This is a test recipe.'
        )

    #Here are the tests
        
    def test_recipe_name(self):
        test_recipe = Recipe.objects.get(recipe_id=1)
        field_label = test_recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_max_length(self):
        test_recipe = Recipe.objects.get(recipe_id=1)
        max_length = test_recipe._meta.get_field('description').max_length
        self.assertEqual(max_length, 120)
