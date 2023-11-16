import os
import glob
import json
import subprocess
from functools import reduce

def GatherAllData(result_file):
    # Зчитує всі дані з result_file та аналізує структуру json 
    result_file.write('Function to gather data from all .json files started')

    dirPath = '.\\'
    files = glob.glob(os.path.join(dirPath, '*.json'))

    result_file.write('\nAll data files have same structure:')
    with open(files[0]) as data_file:
        one_file_data = json.load(data_file)
        result_file.write('\nMain info:')
        result_file.write(f'\nType of entire document: {type(one_file_data).__name__}')
        result_file.write(f'\nDocument has: {len(one_file_data)} elements')
        result_file.write(f'\nType of every element: {[type(one_file_data[elem]).__name__ for elem in one_file_data.keys()]}:')
        result_file.write(f"\nType of 'main' element: {type(one_file_data['main']).__name__}")
        result_file.write(f"\nValue of 'main':\n{one_file_data['main']}")
        result_file.write("\nSubelements of 'main':\n")
        result_file.write('\n'.join([ str(subvalue) for subvalue in one_file_data['main'].items() ]))
        
    data = []

    for file in files:
        with open(file) as data_file:
            filename = os.path.split(file)[1]
            temp = json.load(data_file)
            data.append({os.path.splitext(filename)[0] : temp})     

    result_file.write('\n\nAll data gathered')
    result_file.write('\nFirst data entry printed for example:\n')   
    json.dump(data[0], result_file, indent=4)
    
    return data

def GetValuesByKey(data, key):
    # Отримує значення з даних за вказаним ключем 
    values = []
    
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                values.append({"value":record[key1][k], "date":key1})

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        values.append({"value": elem[key], "date":key1})

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    values.append({"value":record[key1][k][key], "date":key1})

    return values
              
def GetValueByKey(result_file, data, key):
    # Записує в result_file значення з даних за вказаним ключем 
    result_file.write(f'\n\nPrint value by key: {key}:')

    values = GetValuesByKey(data, key)
    for value in values:
        result_file.write(f'\nValue of key: {key} is {value["value"]} on {value["date"]}')
              
def GetMaxValueByKey(result_file, data, key):
    # Записує в result_file максимальне значення з даних за вказаним ключем 
    result_file.write(f'\n\nPrint max value by key: {key}:')
    
    values = GetValuesByKey(data, key)
    maxPair = max(values, key=lambda value: value["value"])

    result_file.write(f'\nMax value of key: {key} is {maxPair["value"]} on {maxPair["date"]}') 
              
def GetAvgValueByKey(result_file, data, key):
    # Записує в result_file середнє значення з даних за вказаним ключем
    result_file.write(f'\n\nPrint average value by key: {key}:')

    values = GetValuesByKey(data, key)
    avg = reduce(lambda prev,current: prev + current["value"], values, 0)

    result_file.write(f'\nAvg value of key: {key} is {avg/len(values)}') 
                
def GetDaysWithParticulatWeatherCondition(result_file, data, key, value):
    # Записує в result_file дні з вказаною погодною умовою
    result_file.write(f'\n\nPrint dates with given value by key: {key}:')

    values = GetValuesByKey(data, key)
    vals = filter(lambda x: x["value"] == value, values)
    for val in vals:
        result_file.write(f'\nValue of key: {key} is {val["value"]} on {val["date"]}')       
              
def GetDaysWithValueMoreThan(result_file, data, key, diff):
    # Записує в result_file дні з значенням більше вказаного
    result_file.write(f'\n\nPrint dates with value bigger then given by key: {key}:')
    
    values = GetValuesByKey(data, key)
    vals = filter(lambda x: x["value"] > diff, values)
    for val in vals:
        result_file.write(f'\nValue of key: {key} is {val["value"]} and is more than {diff} on {val["date"]}')
    
def runSubprocess():
    # Запускає підпроцес на мові C#
    print('Run subprocess')
    subprocess.run(['.\\Release\\script.exe', '16-11-2023.json'])  
    print('Subprocess ended')
              
def main():
    with open('.\\result.txt', 'w') as result_file:
        data = GatherAllData(result_file)
        GetValueByKey(result_file, data, 'temp_max')
        GetMaxValueByKey(result_file, data, 'temp')
        GetAvgValueByKey(result_file, data, 'humidity')
        GetDaysWithParticulatWeatherCondition(result_file, data, 'main', 'Clouds')
        GetDaysWithValueMoreThan(result_file, data, 'humidity', 98)
    runSubprocess()
    
main()
