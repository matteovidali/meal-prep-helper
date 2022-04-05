from ingredient import Ingredient, Unit

# Other things to consider! - getting nutrition info and recipe time

class Recipe:
  def __init__(self, recipe_name, cal = 0, servings = 1, ingredients: list = None, price = 0):
    self.name = recipe_name
    self.calories = cal
    self.num_serv = servings
    self.ingredients = ingredients
    self.price = price

  # Compute total recipe price
  def compute_price(self):
    return sum([ingredient.price for ingredient in self.ingredients]) if not self.price else self.price

  # Compute calories per serving
  # Gives the total price of each ingredient summed unless outside price is provided
  def compute_calories(self):
    return sum([ingredient.calories for ingredient in self.ingredients]) if not self.calories else self.calories

  # Make shopping list
  def make_shopping_list(self):
    pass