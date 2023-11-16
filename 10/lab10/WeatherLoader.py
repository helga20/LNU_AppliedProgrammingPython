import os
import json
import glob
import urllib.request
from datetime import date
from pprint import pprint

# Функція для конструювання URL для OpenWeatherMap API з використанням наданого apiKey
def GetServerAddress(apiKey):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Lviv&appid=$$apiKey$$'
    return url.replace('$$apiKey$$', apiKey)

# Функція для отримання даних з сервера та збереження їх у файл
def GetDataFromServer():   
    print('Checking if file with data for this day already exist')
    
    dirPath = '.\\' # Визначення шляху каталогу, де будуть зберігатися файли даних
    files = glob.glob(os.path.join(dirPath, '*.json')) # Отримання списку всіх файлів у каталозі з розширенням .json
    today = date.today().strftime('%d-%m-%Y') # Отримання поточної дати у форматі 'дд-мм-рррр'
    filename = dirPath + f'{today}.json' # Конструювання імені файлу за поточну дату

    # Перевірка, чи існує файл з таким самим ім'ям (на сьогоднішню дату)
    if filename in files:
        print('File with data for this day already exist')
        return

    print('Connecting to server...')

    remoteaddr = GetServerAddress('1952efb4a7da640d955fd67682858a7f') # Отримання URL для OpenWeatherMap API з використанням наданого API ключа
    remotefile = urllib.request.urlopen(remoteaddr) # Відкриття URL та отримання віддаленого файлу

    print('Get file')

    # Збереження даних віддаленого файлу в локальний файл із поточною датою як ім'ям файлу
    with open(filename, 'wb') as fsave:     
        fsave.write(remotefile.read())  
        print('File was saved')

    remotefile.close() # Закриття віддаленого файлу
    print('Remote file closed')

    print('\nPrint file to python window: ')  
    # Відкриття локального файлу та завантаження його вмісту як JSON об'єкт у змінну data 
    with open(filename) as data_file:
        data = json.load(data_file)
    pprint(data)

    print('\nPrinting finished')

 # Головна функція для виклику GetDataFromServer()   
def main():
    GetDataFromServer()
    
main()
