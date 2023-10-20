import os
import os.path
import glob
import time

# Функція для виведення форматованого представлення імені файлу та часу створення.
def prityPrint(name, time):
    print(f'{name} - {time.tm_mday}.{time.tm_mon}.{time.tm_year} {time.tm_hour}:{time.tm_min}:{time.tm_sec}')

# Основна функція завдання 1.
def task1():
    # Отримання абсолютного шляху до поточної папки програми.
    programDir = os.path.abspath('.')
    
    # Створення шляху до папки "Test1" в поточній папці.
    testDir = os.path.join(programDir, 'Test1')
    
    # Отримання списку файлів у папці "Test1".
    filesAtDir = glob.glob(os.path.join(testDir, '*'))
    
    # Створення пустого списку для зберігання імен файлів та їх часу створення.
    fileNamesWithTime = []
    
    print('Список усіх файлів із зазначенням часу створення:')
    
    # Ітерація через всі файли у папці "Test1".
    for path in filesAtDir:
        head, fileName = os.path.split(path)
        globalCreatedTime = os.path.getmtime(path)
        localCreatedTime = time.localtime(globalCreatedTime)
        
        # Виклик функції для форматованого виведення імені та часу створення файлу.
        prityPrint(fileName, localCreatedTime)
        
        # Додавання імені файлу та часу створення до списку.
        fileNamesWithTime.append({'name': fileName, 'time': localCreatedTime})
    
    print()
    
    # Сортування списку файлів за часом створення.
    fileNamesWithTime.sort(key = lambda x: x['time'])
    
    # Отримання кількості файлів у списку.
    fileNamesWithTimeLength = len(fileNamesWithTime)
    
    # Якщо є принаймні два файли, то вивести найстаріший та найновіший.
    if fileNamesWithTimeLength == 2:
        print('Тільки 2 файли в папці. Найстаріший і найновіший файли:')
        prityPrint(fileNamesWithTime[0]['name'], fileNamesWithTime[0]['time'])
        prityPrint(fileNamesWithTime[1]['name'], fileNamesWithTime[1]['time'])
    
    # Якщо є більше двох файлів, вивести два найстаріших та два найновіших.
    elif fileNamesWithTimeLength > 2:
        print('Два найстаріші файли:')
        prityPrint(fileNamesWithTime[0]['name'], fileNamesWithTime[0]['time'])
        prityPrint(fileNamesWithTime[1]['name'], fileNamesWithTime[1]['time'])
        print()
        print('Два найновіші файли:')
        prityPrint(fileNamesWithTime[fileNamesWithTimeLength-1]['name'], fileNamesWithTime[fileNamesWithTimeLength-1]['time'])
        prityPrint(fileNamesWithTime[fileNamesWithTimeLength-2]['name'], fileNamesWithTime[fileNamesWithTimeLength-2]['time'])

if __name__ == '__main__':
    task1()
