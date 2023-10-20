import os
import os.path
import glob
import subprocess
import time

def task3():
    programDir = os.path.abspath('.')
    print(f"Program folder: {programDir}")
    testDir = os.path.join(programDir, "Test")
    print(f"Test folder: {programDir}")
    testCFile = os.path.join(testDir, 'TestC.exe')
    print(f"Get TestC.exe file")

    parprog = subprocess.Popen([testCFile])
    time.sleep(5)
    print("Finish sub proces first time")

    testFilePath = os.path.join(testDir, "test.txt")
    with open(testFilePath, "r") as data:
        lines = data.readlines()
        numbers = lines[len(lines)-1].split(" ")
        a = int(numbers[1])
        b = int(numbers[2])
        
    with open(testFilePath, "a") as data:
        data.write(f"\nMain: {b} {a+b}")
    print("Finish main proces")
    
    parprog = subprocess.Popen([testCFile])
    time.sleep(5)
    print("Finish sub proces second time")
    

if __name__ == '__main__':
    task3()
