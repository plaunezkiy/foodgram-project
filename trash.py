import csv
from recipes.models import Ingredient

with open('ingredients.csv') as f:
    reader = csv.reader(f)
    for row in reader[:3]:
        print(row)
