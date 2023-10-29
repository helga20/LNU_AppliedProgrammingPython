import urllib.request
import time
import os
import json
from pprint import pprint

def task1(filename):
    print('Loading...') # вивід повідомлення, щоб вказати користувачеві процес завантаження розпочався
    url = 'https://raw.githubusercontent.com/LearnWebCode/json-example/master/animals-1.json'
    remoteFile = urllib.request.urlopen(url) # відкриття файлу за посиланням

    print('Get file from server') # вивід повідомлення для підтвердження успішного отримання файлу з сервера
    with open(filename, 'wb') as file: # відкриття файлу для запису в бінарному режимі
        file.write(remoteFile.read())  # запис вмісту файлу з веб-сервера в локальний файл
        print('File was saved') # вивід повідомлення для підтвердження успішного запису файлу
    
    remoteFile.close() # закриття віддаленого файлу
    print('File closed')

def task2(filename):
    print('\nPrint file to console: ')
    with open(filename) as data_file:
        data = json.load(data_file) # розпарсування JSON-даних з локального файлу
    pprint(data) # вивід розпарсованих даних на консоль

    print('\nPrinting finished') 
    print('Openning file...')
    os.startfile(filename)  # відкриття локального файлу у стандартній програмі для перегляду файлів

def main():
    filename = os.path.join(os.path.abspath("."), "test.json")  # створення шляху до локального файлу
    task1(filename)  # завантаження та збереження даних
    task2(filename)  # читання та виведення даних


if __name__ == "__main__":
    main()
