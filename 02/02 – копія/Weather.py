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
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    minRecord = dataByRange[0]
    for record in dataByRange:
        if minRecord[propertyName] > record[propertyName]:
            minRecord = record
    return minRecord

def getAverageByProperty(data, propertyName, city = None, dateRange = None):
    average = 0.0
    dataByRange = getByCityAndDateRange(data, city, dateRange)
    if len(dataByRange) > 0:
        for record in dataByRange:
            average += float(record[propertyName])
        return average/len(dataByRange)
    else:
        return 0;

def getRecordsWherePropertyMoreThan(data, propertyName, value, dateRange = None):
    dataByRange = getByCityAndDateRange(data, None, dateRange)
    result = []
    for record in dataByRange:
        if record[propertyName] > value:
            result.append(record)
    return result

def printInFormat(record):
    return f"{record['City']}, {record['Country']} ({record['Date']}): \n"+\
        f"\t Температура: {record['Temperature']} °C \n"+\
        f"\t Швидкість вітру: {record['Wind Speed']} м/с \n"+\
        f"\t Тиск: {record['Pressure']} мм рт. ст. \n"+\
        f"\t Вологість: {record['Humidity']}% \n"+\
        f"\t Опади: {record['Precipitation']} мм \n"+\
        f"\t Ймовірність опадів: {record['Probability Precipitation']} %"

def inputCommand():
    return input("Введіть команду: ").split(' ')

def printToFile(outputFilePath, line):
    file = open(outputFilePath, 'a', encoding='utf-8')
    print(line)
    file.write(line + '\n')
    file.close()

def printHelp():
    print('Для старту введіть одну з перелічених команд\n'+
          '\t 1. stop - Зупинка виконання.\n'+
          '\t 2. city_date <city> <date> - Пошук погоди в певному місті на певну дату.\n'+
          '\t 3. min_temperature <date_from> <date_to> - Знаходження найнижчої температури на проміжку часу від date_from до date_to.\n'+
          '\t 4. avg_pressure <city> - Знаходження середнього значення тиску в заданому місті.\n'+
          '\t 5. temperature_dynamics <city> <date_from> <date_to> - Динаміка зміни температури в певному місті на проміжку часу від date_from до date_to.\n'+
          '\t 6. precipitation_more_than <value> - Знаходження міст, у яких опади більше ніж value.\n')
    
def main():
    data = getData('WeatherForWeek.txt')
    
    printHelp()
    outputFilePath = input("Введіть назву файлу для запису результатів: ")
    
    file = open(outputFilePath, 'w', encoding='utf-8')
    file.close()
    
    command = inputCommand()
    while command[0] != 'stop':
        
        if command[0] == 'city_date':
            if len(command) == 1:
                result = getByCityAndDate(data)
            elif len(command) == 2:
                result = getByCityAndDate(data, command[1])
            elif len(command) == 3:
                result = getByCityAndDate(data, command[1], datetime.datetime.strptime(command[2], '%d/%m/%Y'))
            for record in result:
                printToFile(outputFilePath, printInFormat(record))
        
        elif command[0] == 'min_temperature':
            if len(command) == 1:
                record = getRecordWithMinProperty(data, 'Temperature')
                printToFile(outputFilePath, f'Мінімальна температура ({record["Temperature"]} °C) в місті {record["City"]}')
            elif len(command) == 3:
                date_from = datetime.datetime.strptime(f'{command[1]}', '%d/%m/%Y')
                date_to =  datetime.datetime.strptime(f'{command[2]}', '%d/%m/%Y')
                record = getRecordWithMinProperty(data, 'Temperature', None, [date_from, date_to])
                printToFile(outputFilePath, f'Мінімальна температура ({record["Temperature"]} °C) на проміжку від {command[1]} до {command[2]} у місті {record["City"]}')
    
        elif command[0] == 'avg_pressure':
            if len(command) == 1:
                printToFile(outputFilePath, 'Середній тиск – {:.2f} мм рт. ст.'.format(getAverageByProperty(data, 'Pressure')))
            elif len(command) == 2:
                printToFile(outputFilePath, 'Середній тиск у місті {} – {:.2f} мм рт. ст.'.format(command[1], getAverageByProperty(data, 'Pressure', command[1])))
       
        elif command[0] == 'temperature_dynamics':
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
            
        elif command[0] == 'precipitation_more_than':
            if len(command) == 2:
                result = getRecordsWherePropertyMoreThan(data, 'Precipitation', float(command[1]))
                resultCities = []
                for record in result:
                    resultCities.append(record['City'])
                printToFile(outputFilePath, f'Опади більші ніж {command[1]} мм в містах: ' + ', '.join(list(set(resultCities))))

        else:        
            print("Неправильна команда. Спробуйте ще раз!")
        command = inputCommand()

if __name__ == '__main__':
    main()



    