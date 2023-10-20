import os
import os.path
import glob
import stat

# Основна функція завдання 3.
def task3():
    # Запитуємо користувача ввести розширення файлів для пошуку.
    extension = input('Будь ласка, введіть потрібне розширення (txt, pdf, xml і т.д.): ')
    
    # Отримання абсолютного шляху до поточної папки програми.
    programDir = os.path.abspath('.')
    
    # Створення шляху до папки "Test3" в поточній папці.
    testDir = os.path.join(programDir, 'Test3')
    
    # Отримання списку підпапок у папці "Test3".
    dirs = os.listdir(testDir)
    
    # "Прапорець", який вказує, чи були знайдені файли з вказаним розширенням.
    anyFiles = False
    
    print(f'\nФайли з {extension} розширенням:')
    
    # Ітерація через підпапки.
    for d in dirs:
        path = os.path.join(testDir, d)
        
        # Отримання списку файлів у поточній підпапці.
        files = os.listdir(path)
        
        # Ітерація через файли в поточній підпапці.
        for file in files:
            # Розділення імені файлу та його розширення.
            root, ext = os.path.splitext(file)
            
            # Перевірка, чи розширення файлу відповідає введеному користувачем.
            if extension in ext:
                print(f'{file} - in {d}')
                anyFiles = True
    
    # Виведення повідомлення, якщо файли з вказаним розширенням не знайдені.
    if not anyFiles:
        print(f"Немає файлів з {extension} розширенням у цій папці.")

if __name__ == '__main__':
    task3()
