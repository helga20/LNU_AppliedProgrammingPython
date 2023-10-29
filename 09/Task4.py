import json
import os
from pprint import pprint

# Функція призначена для виведення інформації про кожну тварину із вхідних даних
def printAnimalInfo(data): 
    """Print information about each animal"""  
    for animal in data:  # початок циклу, який проходиться по кожному об'єкту в списку data
        print(f"\nAnimal:") 
        for key, value in animal.items():  # цикл для ітерації по ключам та значенням словника, який представляє кожну окрему тварину
            if key == 'foods':  # перевірка, чи ключ дорівнює 'foods', означаючи інформацію про їжу тварини
                print(f"{key}:")  # виведення ключа 'foods' для позначення початку інформації про їжу
                for food_key, food_value in value.items():  # цикл для ітерації по ключам та значенням словника, який представляє інформацію про їжу
                    print(f"\t{food_key}: {food_value}")  # виведення інформації про конкретний вид їжі
            else:
                print(f"{key}: {value}")  # виведення інших ключів та їхніх значень (окрім 'foods')

# Функція дозволяє знаходити і виводити всі значення, які відповідають заданому ключу у структурі даних data
def findValuesByKey(data, key):
    """ Find all values by key """
    print(f'Find all values by key: {key}') # виведення повідомлення про початок пошуку
    for animal in data: # початок циклу, який проходиться по кожному об'єкту в списку data
        findValuesByKeyHelper(animal, key) # виклик функції-допоміжника для пошуку значень за ключем

# Функція-допоміжник для рекурсивного пошуку значень за ключем у структурі даних data
def findValuesByKeyHelper(data, key): 
    """ Find all values by key recursive helper """ 
    if isinstance(data, dict):  # перевірка, чи об'єкт 'data' є словником
        for k, v in data.items():  # цикл для ітерації по ключах та значенням у словнику 'data'
            if k == key:  # перевірка, чи поточний ключ відповідає шуканому ключу
                print(f'\t{v}')  # виведення значення 'v', якщо ключ відповідає шуканому ключу
            else:
                findValuesByKeyHelper(v, key)  # рекурсивний виклик функції-допоміжника для пошуку в підструктурах

# Функція дозволяє знаходити і виводити всі об'єкти, які містять задану пару ключ-значення у структурі даних data
def findByKeyValuePair(data, key, value):
    """ Find object by key value """
    print(f'\nPrint {key} with value {value}') # виведення повідомлення про початок пошуку
    for animal in data: # початок циклу, який проходиться по кожному об'єкту (тварині) в списку 'data'
        findByKeyValuePairHelper(animal, key, value) # виклик функції-допоміжника для пошуку об'єктів за ключем та значенням

# Функція-допоміжник для рекурсивного пошуку об'єктів за парою ключ-значення у структурі даних data
def findByKeyValuePairHelper(data, key, value):
    """ Find object by key value recursive helper """  
    if isinstance(data, dict):  # перевірка, чи об'єкт 'data' є словником
        if data.get(key) == value:  # перевірка, чи в словнику є ключ 'key' і чи його значення дорівнює заданому значенню 'value'
            pprint(data)  # виведення об'єкту, якщо умова виконується

def task4(filename):
    print('Reading file...')  
    with open(filename) as data_file:  # відкриття файлу для читання та створення контекстного менеджера
        data = json.load(data_file)  # завантаження JSON-даних з файлу та збереження їх у змінній 'data'
    
    printAnimalInfo(data)  # виклик функції для виведення інформації про тварини
    findValuesByKey(data, 'name')  # виклик функції для пошуку значень за ключем 'name'
    findByKeyValuePair(data, 'species', 'cat')  # виклик функції для пошуку об'єктів за ключем 'species' і значенням 'cat'

def main():
    filename = os.path.join(os.path.abspath("."), "test.json")
    task4(filename)

if __name__ == "__main__":
    main()
