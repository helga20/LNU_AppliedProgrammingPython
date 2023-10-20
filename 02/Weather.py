import csv
import datetime

properties = {
    'city': 'City',
    'country': 'Country',
    'date': 'Date',
    'temperature': 'Temperature',
    'wind_speed': 'Wind Speed',
    'pressure': 'Pressure',
    'humidity': 'Humidity',
    'precipitation': 'Precipitation',
    'probability_precipitation': 'Probability Precipitation',
}

propertiesList = list(properties.values())

def getData(fileName):

    """
    Отримання даних з файлу:
    fileName - шлях до файлу   
    Формат введення даних повинен бути:
	City,Country,Date,Temperature,Wind Speed,Pressure,Humidity,Precipitation,Probability Precipitation       
    Вихідний формат:
        [{
            City: value,
            Country: value,
            Date: value,
            Temperature: value,
            Wind Speed: value,
            Pressure: value,
            Humidity': value,
            Precipitation: value,
            Probability Precipitation: value
        }, ...
        ]
    """

    data = []
    with open(fileName, newline='') as file:
        weather_reader = csv.DictReader(file, delimiter=',', quotechar='"')
        for row in weather_reader:
            newRow = row
            newRow['Date'] = datetime.datetime.strptime(row['Date'], '%d/%m/%Y')
            newRow['Temperature'] = float(row['Temperature'])
            newRow['Wind Speed'] = float(row['Wind Speed'])
            newRow['Pressure'] = float(row['Pressure'])
            newRow['Humidity'] = float(row['Humidity'])
            newRow['Precipitation'] = float(row['Precipitation'] if row['Precipitation'] else '0')
            newRow['Probability Precipitation'] = float(row['Probability Precipitation'] if row['Probability Precipitation'] else '0')
            data.append(row)
    return data

def getByCityAndDate(data, city = None, date = None):

    """ 
    Отримання списку записів погоди за значенням міста і дати:
    data - список, який містить записи про погоду
    city - назва міста (необов'язково) 
    date - дата (необов'язково)
    """

    result = []
    if city is not None and date is not None:
        for record in data:
            if record['City'] == city and record['Date'] == date:
                result.append(record)
    elif city is not None and date is None:
        for record in data:
            if record['City'] == city:
                result.append(record)
    elif city is None and date is not None:
        for record in data:
            if record['Date'] == date:
                result.append(record)
    else:
        return data
    return result

def getByCityAndDateRange(data, city = None, dateRange = None):
    
    """ 
    Отримання списку погоди за містом і проміжок дат:
    data - список, який містить записи про погоду
    city - назва міста (необов'язково) 
    dateRange - проміжок дат (необов'язково) 
    """

    result = []
    if city is not None and dateRange is not None:
        for record in data:
            if record['City'] == city and (record['Date'] >= dateRange[0] and record['Date'] <= dateRange[1]):
                result.append(record)
    elif city is not None and dateRange is None:
        for record in data:
            if record['City'] == city:
                result.append(record)
    elif city is None and dateRange is not None:
        for record in data:
            if record['Date'] >= dateRange[0] and record['Date'] <= dateRange[1]:
                result.append(record)
    else:
        return data
    return result

def getRecordWithMinProperty(data, propertyName, city = None, dateRange = None):

    """
    Отримання запису із мінімальним значенням певної властивості:
    data - список, який містить записи про погоду
    propertyName - назва властивості, значення якої обробляється
    city - назва міста (необов'язково) 
    dateRange - проміжок дат (необов'язково) 
    """

    dataByRange = getByCityAndDateRange(data, city, dateRange)
    minRecord = dataByRange[0]
    for record in dataByRange:
        if minRecord[propertyName] > record[propertyName]:
            minRecord = record
    return minRecord

def getRecordWithMaxProperty(data, propertyName, city = None, dateRange = None):

    """
    Отримання запису із максимальним значенням певної властивості:
    data - список, який містить записи про погоду
    propertyName - назва властивості, значення якої обробляється
    city - назва міста (необов'язково) 
    dateRange - проміжок дат (необов'язково) 
    """
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    maxRecord = dataByRange[0]
    for record in dataByRange:
        if maxRecord[propertyName] < record[propertyName]:
            maxRecord = record
    return maxRecord

def getAverageByProperty(data, propertyName, city = None, dateRange = None):

    """
    Отримання середнього значення певної властивості:
    data - список, який містить записи про погоду
    propertyName - назва властивості, значення якої обробляється
    city - назва міста (необов'язково) 
    dateRange - проміжок дат (необов'язково)    
    """

    average = 0.0
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    if len(dataByRange) > 0:
        for record in dataByRange:
            average += float(record[propertyName])
        return average/len(dataByRange)
    else:
        return 0;

def getRecordsWherePropertyLessThan(data, propertyName, value, dateRange = None):
    
    """
    Отримання значення, де певна властивість менша ніж задане значення:
    data - список, який містить записи про погоду
    propertyName - назва властивості, значення якої обробляється
    value - значення для порівняння
    dateRange - проміжок дат (необов'язково)
    """
    
    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] < value:
            result.append(record)
    return result

def getRecordsWherePropertyMoreThan(data, propertyName, value, dateRange = None):

    """
    Отримання значення, де певна властивість більша ніж задане значення:
    data - список, який містить записи про погоду
    propertyName - назва властивості, значення якої обробляється
    value - значення для порівняння
    dateRange - проміжок дат (необов'язково)
    """

    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] > value:
            result.append(record)
    return result


def getRecordsWherePropertyEqual(data, propertyName, value, dateRange = None):
   
    """
    Отримання значення, де певна властивість дорівнює заданому значенню:
    data - список, який містить записи про погоду
    propertyName - назва властивості, значення якої обробляється
    value - значення для порівняння
    dateRange - проміжок дат (необов'язково)
    """

    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] == value:
            result.append(record)
    return result

def printInFormat(record):

    """ 
    Форматування даних про погоду 
    """

    return f"{record['City']}, {record['Country']} ({record['Date']}): \n"+\
        f"\t Температура: {record['Temperature']} °C \n"+\
        f"\t Швидкість вітру: {record['Wind Speed']} м/с \n"+\
        f"\t Тиск: {record['Pressure']} мм рт. ст. \n"+\
        f"\t Вологість: {record['Humidity']}% \n"+\
        f"\t Опади: {record['Precipitation']} мм \n"+\
        f"\t Ймовірність опадів: {record['Probability Precipitation']} %"

def inputCommand():

    """
    Введення команди з консолі
    """

    return input("Введіть команду: ").split(' ')

def printToFile(outputFilePath, line):

    """
    Друкування рядків у файл і консоль
    outputFilePath - шлях до файлу
    line - рядок для написання
    """

    file = open(outputFilePath, 'a', encoding='utf-8')
    print(line)
    file.write(line + '\n')
    file.close()

def printHelp():
    print('Для старту введіть одну з перелічених команд\n'+
          '\t 1. stop - Зупинка виконання.\n'+
          '\t 2. city_date <city> <date> - Пошук погоди в певному місті на певну дату.\n'+
          '\t 3) min_temperature <date_from> <date_to> - Знаходження найнижчої температури на проміжку часу від date_from до date_to.\n'+
          '\t 4) max_temperature <date_from> <date_to> - Знаходження найвищої температуру на проміжку часу від date_from до date_to.\n'+
          '\t 5) avg_wind_speed <city> - Знаходження середнього значення швидкості вітру в заданому місті.\n'+
          '\t 6) avg_pressure <city> - Знаходження середнього значення тиску в заданому місті.\n'+
          '\t 7) temperature_dynamics <city> <date_from> <date_to> - Динаміка зміни температури в певному місті на проміжку часу від date_from до date_to.\n'+
          '\t 8) prob_precipitation_less_than <value> - Знаходження міст, у яких ймовірність опадів менша ніж value.\n'+
          '\t 9) precipitation_more_than <value> - Знаходження міст, у яких опади більше ніж value.\n'+
          '\t 10) humidity_equal <value> <date_from> <date_to> - Знаходження міст, у яких вологість дорівнює value від date_from до date_to (можна вказати тільки value).\n'+
          '! Формат дати повинен бути таким: День/Місяць/Рік !'+
          '\n! Доступні міста: Kyiv, Lviv, Rome, Warsaw !\n')
    

def main():
    data = getData('WeatherForWeek.csv')
    
    printHelp()
    outputFilePath = input("Введіть назву файлу для запису результатів: ")
    
    file = open(outputFilePath, 'w', encoding='utf-8')
    file.close()
    
    command = inputCommand()
    while command[0] != 'stop':
        
        if command[0] == 'city_date':
            #приклад команди: city_date Kyiv 13/09/2023
            #приклад команди: city_date Kyiv 
            #приклад команди: city_date 13/09/2023
            #приклад команди: city_date
            if len(command) == 1:
                result = getByCityAndDate(data)
            elif len(command) == 2:
                result = getByCityAndDate(data, command[1])
            elif len(command) == 3:
                result = getByCityAndDate(data, command[1], datetime.datetime.strptime(command[2], '%d/%m/%Y'))
            for record in result:
                printToFile(outputFilePath, printInFormat(record))
        
        elif command[0] == 'min_temperature':
            #приклад команди: min_temperature
            #приклад команди: min_temperature 13/09/2023 15/09/2023

            if len(command) == 1:
                record = getRecordWithMinProperty(data, 'Temperature')
                printToFile(outputFilePath, f'Мінімальна температура ({record["Temperature"]} °C) в місті {record["City"]}')
            elif len(command) == 3:
                date_from = datetime.datetime.strptime(f'{command[1]}', '%d/%m/%Y')
                date_to =  datetime.datetime.strptime(f'{command[2]}', '%d/%m/%Y')
                record = getRecordWithMinProperty(data, 'Temperature', None, [date_from, date_to])
                printToFile(outputFilePath, f'Мінімальна температура ({record["Temperature"]} °C) на проміжку від {command[1]} до {command[2]} у місті {record["City"]}')
        
        elif command[0] == 'max_temperature':
            #приклад команди: max_temperature
            #приклад команди: max_temperature 13/09/2023 15/09/2023

            if len(command) == 1:
                record = getRecordWithMaxProperty(data, 'Temperature')
                printToFile(outputFilePath, f'Максимальна температура ({record["Temperature"]} °C) в місті {record["City"]}')
            elif len(command) == 3:
                date_from = datetime.datetime.strptime(f'{command[1]}', '%d/%m/%Y')
                date_to =  datetime.datetime.strptime(f'{command[2]}', '%d/%m/%Y')
                record = getRecordWithMaxProperty(data, 'Temperature', None, [date_from, date_to])
                printToFile(outputFilePath, f'Максимальна температура ({record["Temperature"]} °C) на проміжку від {command[1]} до {command[2]} у місті {record["City"]}')
        
        elif command[0] == 'avg_wind_speed':
            #приклад команди: avg_wind_speed
            #приклад команди: avg_wind_speed Lviv

            if len(command) == 1:
                printToFile(outputFilePath, 'Середня швидкість вітру – {:.2f} м/с'.format(getAverageByProperty(data, 'Wind Speed')))
            elif len(command) == 2:
                printToFile(outputFilePath, 'Середня швидкість вітру в місті {} – {:.2f} м/с'.format(command[1], getAverageByProperty(data, 'Wind Speed', command[1])))
       
        elif command[0] == 'avg_pressure':
            #приклад команди: avg_pressure
            #приклад команди: avg_pressure Lviv

            if len(command) == 1:
                printToFile(outputFilePath, 'Середній тиск – {:.2f} мм рт. ст.'.format(getAverageByProperty(data, 'Pressure')))
            elif len(command) == 2:
                printToFile(outputFilePath, 'Середній тиск у місті {} – {:.2f} мм рт. ст.'.format(command[1], getAverageByProperty(data, 'Pressure', command[1])))
       
        elif command[0] == 'temperature_dynamics':
            #приклад команди: temperature_dynamics Lviv 
            #приклад команди: temperature_dynamics Lviv 13/09/2023 15/09/2023

            result = []
            if len(command) == 2:
                result = getByCityAndDateRange(data, command[1])
            elif len(command) == 4:
                date_from = datetime.datetime.strptime(f'{command[2]}', '%d/%m/%Y')
                date_to =  datetime.datetime.strptime(f'{command[3]}', '%d/%m/%Y')
                result = getByCityAndDateRange(data, command[1], [date_from, date_to])
                printToFile(outputFilePath, f'Динаміка зміни температури в місті {command[1]} з {command[2]} до {command[3]} :')
            temperatureRecords = []
            for record in result:
                temperatureRecords.append(str(record["Temperature"]))
            printToFile(outputFilePath, '°C '.join(temperatureRecords) + '°C')

        elif command[0] == 'prob_precipitation_less_than':
            #приклад команди: prob_precipitation_less_than 40 

            if len(command) == 2:
                result = getRecordsWherePropertyLessThan(data, 'Probability Precipitation', float(command[1]))
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                printToFile(outputFilePath, f'Ймовірність опадів менша ніж {command[1]} % в містах: ' + ', '.join(list(set(resultCities))))
            
        elif command[0] == 'precipitation_more_than':
            #приклад команди: precipitation_more_than 0.2

            if len(command) == 2:
                result = getRecordsWherePropertyMoreThan(data, 'Precipitation', float(command[1]))
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                printToFile(outputFilePath, f'Опади більші ніж {command[1]} мм в містах: ' + ', '.join(list(set(resultCities))))

        elif command[0] == 'humidity_equal':
            #приклад команди: humidity_equal 60
            #приклад команди: humidity_equal 49 13/09/2023 15/09/2023

            if len(command) == 2:
                result = getRecordsWherePropertyEqual(data, 'Humidity', float(command[1]))
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                printToFile(outputFilePath, f'Вологість рівна {command[1]} % в містах: ' + ', '.join(list(set(resultCities))))
            elif len(command) == 4:
                date_from = datetime.datetime.strptime(f'{command[2]}', '%d/%m/%Y')
                date_to =  datetime.datetime.strptime(f'{command[3]}', '%d/%m/%Y')
                probability = float(command[1])
                result = getRecordsWherePropertyEqual(data, 'Humidity', probability, [date_from, date_to])
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                printToFile(outputFilePath, f'Вологість рівна {command[1]} % з {command[2]} до {command[3]} у містах: ' + ', '.join(list(set(resultCities))))

        else:        
            print("Неправильна команда. Спробуйте ще раз!")
        command = inputCommand()

if __name__ == '__main__':
    main()



    