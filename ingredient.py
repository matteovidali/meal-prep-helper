from ast import Str
from enum import Enum, auto

# An enum to easily use units in the future
class Unit(Enum):
  l = 'l'
  ml = 'ml'
  kg = 'kg'
  g = 'g'
  unit = 'unit' # Thnis may be annoying to deal with

class Ingredient:
  
  def __init__(self, name: str, price: float = 0, quantity: float = 1, unit: Str = 'g', calories: int = 0):
    self.name = name
    self.quantity = quantity
    self.price = price
    self.unit = Unit[unit]
    self.calories = calories
    self.calories_per_unit = calories/quantity
    self.price_per_unit = price/quantity
  
  def get_price(self, per_unit=False):
    return self.price_per_unit if per_unit else self.price


if __name__ == "__main__":

  carrot = Ingredient('Carrot', 10.5, 10, 'g')
  print(carrot.name)
  print(carrot.get_price())
  print(carrot.unit)