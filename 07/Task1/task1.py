import os
import os.path
import glob

def task1():
    programDir = os.path.abspath('.')
    print(f"Program folder: {programDir}")
    testDir = os.path.join(programDir, 'Test1')
    print(f"Test folder: {testDir}")
    bmpFile = glob.glob(os.path.join(testDir, '*.bmp'))[0]
    print(f"Get .bmp file path {bmpFile}")
    wordFile = glob.glob(os.path.join(testDir, '*.docx'))[0]
    print(f"Get .docx file path {wordFile}")
    os.startfile(bmpFile)
    print(f"Start .bmp file")
    os.startfile(wordFile)
    print(f"Start .docx file")

if __name__ == '__main__':
    task1()
