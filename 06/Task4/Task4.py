import os
import os.path
import glob
import stat

# Основна функція завдання 4.
def task4():
    # Отримання абсолютного шляху до поточної папки програми.
    programDir = os.path.abspath('.')
    
    # Створення шляху до папки "Test4" в поточній папці.
    testFolder = os.path.join(programDir, 'Test4')
    
    # Отримання списку файлів у папці "Test4".
    filesAtDir = glob.glob(os.path.join(testFolder, '*'))
    
    # Список для зберігання інформації про файли разом із їх розширеннями.
    fileWithExtensions = []
    
    # Список для зберігання унікальних розширень.
    uniqueExtensions = []
    
    # Ітерація через файли у папці "Test4".
    for path in filesAtDir:
        root, ext = os.path.splitext(path)
        head, filename = os.path.split(path)
        
        # Перевірка, чи розширення файлу вже додане до списку унікальних розширень.
        if ext not in uniqueExtensions:
            uniqueExtensions.append(ext)
        
        # Додавання інформації про файл у список.
        fileWithExtensions.append({'path': path, 'name': filename, 'ext': ext})
    
    # Виведення унікальних розширень.
    print(uniqueExtensions)
    
    # Створення нової папки для кожного унікального розширення.
    for extension in uniqueExtensions:
        newDirName = os.path.join(programDir, f'Test_{extension[1:]}')  # extension[1:] - відкидає крапку з розширення.
        os.mkdir(newDirName)
    
    print('Нова папка створена')
    
    # Переміщення файлів у відповідні папки згідно їх розширення.
    for file in fileWithExtensions:
        newDirName = os.path.join(programDir, f'Test_{file["ext"][1:]}')
        newFileName = os.path.join(newDirName, file["name"])
        
        # Зміна прав доступу до файлу перед переміщенням.
        os.chmod(file['path'], stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        
        # Переміщення файлу у нову папку.
        os.replace(file['path'], newFileName)
    
    print('Файли переміщено')

if __name__ == '__main__':
    task4()
