class Ingredient(object):
    def __init__(self, name) -> None:
        self.name = name
class Recipe(object):
    ingredients = ()
    
    def __init__(self, name: str) -> None:
        self.name = name

    def add_ingredient(self, ingredient_name: Ingredient, quantity: int):
        self.ingredients += ((ingredient_name, quantity))

    def __len__(self):
        return len(self.ingredients)

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return self.ingredients[num]
