import os
import os.path
import glob
import time

# Функція для отримання списку файлів у заданій папці разом із їх розмірами.
def getFilesList(directory):
    files = []
    for file in os.listdir(directory):
        size = os.path.getsize(os.path.join(directory, file))
        files.append((file, size))
    return files

# Основна функція завдання 2.
def task2():
    # Отримання абсолютного шляху до поточної папки програми.
    programDir = os.path.abspath('.')
    
    # Створення шляху до папки "Test2" в поточній папці.
    testDir = os.path.join(programDir, 'Test2')
    
    # Створення шляхів до папок "Folder1" та "Folder2" у "Test2".
    dir1Path = os.path.join(testDir, 'Folder1')
    dir2Path = os.path.join(testDir, 'Folder2')
    
    # Отримання списку файлів у "Folder1" та "Folder2" разом із їх розмірами.
    files1 = getFilesList(dir1Path)
    files2 = getFilesList(dir2Path)
    
    # Знайдення дубльованих файлів у "Folder1" та "Folder2".
    intersection = [value for value in files1 if value in files2]
    
    print('Дубльовані файли у Folder1 та Folder2:')
    
    # Виведення імен та розмірів дубльованих файлів.
    for file in intersection:
        print(f'{file[0]} \t - {file[1]} байтів')

if __name__ == '__main__':
    task2()
