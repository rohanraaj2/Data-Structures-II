class Ingredient(object):
    def __init__(self, name) -> None:
        self.name = name
class Recipe(object):
    ingredients = []
    num = -1
    
    def __init__(self, name: str) -> None:
        self.name = name

    def add_ingredient(self, ingredient_name: Ingredient, quantity: int):
        self.ingredients.append((ingredient_name.name, quantity))

    def __len__(self):
        return len(self.ingredients)

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.ingredients[self.num]