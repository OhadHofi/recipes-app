import requests
from .db_manager import db_manager


async def fetch_recipes(ingredient, dairy, gluten):
    recipes = requests.get(
        f'https://recipes-goodness.herokuapp.com/recipes/{ingredient}')
    recipes = recipes.json()

    recipes = [{"ingredients": recipe["ingredients"],
                "title": recipe["title"],
                "thumbnail": recipe["thumbnail"],
                "href": recipe["href"]}
               for recipe in recipes["results"]
               if filter_dairy(dairy, recipe) or filter_gluten(gluten, recipe)]

    return recipes


def filter_dairy(dairy, recipe):
    if dairy:
        dairies = db_manager.get_dairy_ingredients()
        for ingredient in recipe["ingredients"]:
            if (ingredient in dairies):
                return False
    return True


def filter_gluten(gluten, recipe):
    if gluten:
        glutens = db_manager.get_gluten_ingredients()
        for ingredient in recipe["ingredients"]:
            if (ingredient in glutens):
                return False
    return True
