import os
import os.path
import glob

def task2():
    programDir = os.path.abspath('.')
    print(f"Program folder: {programDir}")
    testDir = os.path.join(programDir, "Test2")
    print(f"Test folder: {programDir}")
    filesAtDir = glob.glob(os.path.join(testDir, '*.txt'))
    print(f"Get .txt files")
    notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
    params = filesAtDir.copy()
    params.insert(0, " ")
    print(f"Start run files:{filesAtDir}")
    os.execvp(notepadPath, params)

if __name__ == '__main__':
    task2()
