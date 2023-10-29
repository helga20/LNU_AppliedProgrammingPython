import json
import os
from pprint import pprint

def task3(filename):
    print('Reading file...') # вивід повідомлення, щоб вказати користувачеві процес завантаження розпочався
    with open(filename) as data_file: # відкриття файлу для читання
        data = json.load(data_file) # розпарсування JSON-даних з локального файлу

    animals = data  # присвоєння змінній animals значення змінної data
    print('Main info:')  
    print(f'\nAmount of animals: {len(animals)}') # вивід кількості елементів у списку animals
    
    typesOfAnimalObjects = [type(animal).__name__ for animal in animals] # створення списку з типів елементів списку animals
    print(f'\nTypes of animal objects: {typesOfAnimalObjects}:') # вивід типів елементів списку animals
    
    typeOfFoodsLikes = type(animals[0]['foods']['likes']).__name__  # створення змінної з типом значення елемента списку animals
    print(f"\nType of 'foods.likes': {typeOfFoodsLikes}") # вивід типу значення елемента списку animals

    valueOfFoodsLikes = animals[0]['foods']['likes'] # створення змінної зі значенням елемента списку animals
    print(f"\nValue of 'foods.likes':\n{valueOfFoodsLikes}") # вивід значення елемента списку animals
    
    print("\nSubobjects of the first animal:") 
    print([subvalue for subvalue in animals[0].items()], sep='\n') # вивід значень елементів списку animals

    allAnimalElements = [str(animal) for animal in animals] # створення списку з елементів списку animals
    print(f'\nAll objects of animals:', allAnimalElements, sep='\n\n') # вивід елементів списку animals

def main():
    filename = os.path.join(os.path.abspath("."), "test.json") # створення шляху до локального файлу
    task3(filename) 

if __name__ == "__main__":
    main()
