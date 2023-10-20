def getData(fileName):

    """
    Отримання даних з файлу:
    fileName - шлях до файлу   
    trumDirection є: forward, backward
        
    Формат введення даних повинен бути:
        tramNumber-trumDirection:stop1-stop2-stop3-...

    Вихідний формат:
    {'tramNumber':
        {
            'forward': [stop1, stop2, stop3],
            'backward': [...]
        },
     'otherTramNumber':
        {
            'forward': [...],
            'backward': [...]
        },
     ...
    }
    """

    data = {}
    file = open(fileName, 'r', encoding='utf-8')
    lines = file.read().split('\n')
    for line in lines:
        splitedRow = line.split(':')
        splitedStops = splitedRow[1].split('–')
        splitedInfo = splitedRow[0].split('–')
        if data.get(splitedInfo[0]):
            data[splitedInfo[0]].update({splitedInfo[1]: splitedStops})
        else:
            data[splitedInfo[0]] = {splitedInfo[1]: splitedStops}
    return data

def printInFormat(data, routeNumber):

    """
    Форматування даних про маршрути трамваїв 
    route - трамвайний маршрут
    """

    if routeNumber in data:
        route = data[routeNumber]
        print(f'Вперед:')
        for stop in route['forward']:
            print(f'\t{stop}')
        print(f'Назад:')
        for stop in route['backward']:
            print(f'\t{stop}')
    else:
        print(f'У Львові немає трамвая з таким номером')


def inputCommand():

    """
    Введення команди користувачем    
    """

    return input("Будь ласка, введіть команду:\n").split(':')


def getTramsOnStation(data, station):

    """
    Отримання всіх трамваїв, які зупиняються на заданій зупинці

    data - список усіх трамвайних маршрутів
    station - назва зупинки
    """

    trams = []
    for record in data:
        if station in data[record]['forward'] or station in data[record]['backward']:
            trams.append(record)
    return trams 

def getIntersection(data, tram1, tram2):

    """
    Отримання зупинки на яких трамваї перетинаються.

    data - список усіх трамвайних маршрутів
    tram1 - ідентифікатор 1 трамвая
    tram2 - ідентифікатор 2 трамвая
    """

    stations = None
    if tram1 in data and tram2 in data:
        stations = {}
        stations['forward'] = [value for value in data[tram1]['forward'] if value in data[tram2]['forward']] 
        stations['backward'] = [value for value in data[tram1]['backward'] if value in data[tram2]['backward']] 
    return stations


def getNumberOfStation(data, station1, station2):

    """
    Отримання кількості зупинок від зупинки1 до зупинки2 без пересадки на інший трамвай

    data -список усіх трамвайних маршрутів 
    station1 - назва початкової зупинки
    station2 - назва кінцевої зупинки
    повертає: номер зупинки, маршрут
    """

    if station1 == station2:
        return 0
    tram = None
    
    for route in data:
        if station1 in data[route]['forward'] and station2 in data[route]['forward']:
            station1Index = data[route]['forward'].index(station1)
            station2Index = data[route]['forward'].index(station2)
            if station1Index < station2Index:       
                number = abs(station1Index - station2Index)
                tram = route
                
        if station1 in data[route]['backward'] and station2 in data[route]['backward']:
            number = abs(data[route]['backward'].index(station1) - data[route]['backward'].index(station2))
            tram = route
    if tram is not None:
        return number, tram
    else:
        return None

 
def getNumberOfStationAtRoute(route, station1, station2):

    """
    Отримайте кількість зупинок від зупинки 1 до зупинки 2 на маршруті

    data - список трамвайного маршруту
    station1 - назва початкової зупинки
    station2 - назва кінцевої зупинки
    повертає: номер зупинки, маршрут
    """
    
    if station1 in route['forward'] and station2 in route['forward']:
        station1Index = route['forward'].index(station1)
        station2Index = route['forward'].index(station2)
        return abs(station1Index - station2Index)
    else:
        station1Index = route['backward'].index(station1)
        station2Index = route['backward'].index(station2)
        return abs(station1Index - station2Index)
 
def getRoute(data, station1, station2):

    """
    Отримання маршруту з зупинки 1 до зупинки 2

    data - список усіх трамвайних маршрутів
    station1 - назва початкової зупинки
    station2 - назва кінцевої зупинки

    якщо без пересадки
        повертає: номер трамваю, маршрут
    якщо з пересадкою
        повертає список [номер першого маршруту, номер другого маршруту, зупинка перетину, перша довжина маршруту, друга довжина маршруту]
    """
    
    trams = []
    route = getNumberOfStation(data, station1, station2)
    if route is not None:
        return route
    else:            
        firstStationTrams = []
        secondStationTrams = []
        for route in data:
            if station1 in data[route]['forward'] or station1 in data[route]['backward']:
                firstStationTrams.append(route)     
                
            if station2 in data[route]['forward'] or station2 in data[route]['backward']:
                secondStationTrams.append(route)
       
        firstLength = 0
        secondLength = 0        
        for i in range(len(firstStationTrams)):
            for j in range(len(secondStationTrams)):
                intersectStations = getIntersection(data, firstStationTrams[i], secondStationTrams[j])
                if len(intersectStations['forward']) != 0 or len(intersectStations['backward']) != 0:
                    firstLength = getNumberOfStation(data, station1, intersectStations['backward'][0])[0]
                    secondLength = getNumberOfStation(data, intersectStations['backward'][0], station2)[0]
                    intersectStation = intersectStations['backward'][0]
                    for station in intersectStations['backward']:
                        tempLength = getNumberOfStation(data, station1, station)
                        if  tempLength is not None and tempLength[0] < firstLength:
                            firstLength = getNumberOfStationAtRoute(data[firstStationTrams[i]], station1, station)
                            secondLength = getNumberOfStationAtRoute(data[secondStationTrams[j]], station, station2)
                            intersectStation = station
                    for station in intersectStations['forward']:
                        tempLength = getNumberOfStation(data, station1, station)
                        if  tempLength is not None and tempLength[0] < firstLength:
                            firstLength = getNumberOfStationAtRoute(data[firstStationTrams[i]], station1, station)
                            secondLength = getNumberOfStationAtRoute(data[secondStationTrams[j]], station, station2)
                            intersectStation = station
       
                    trams.append([firstStationTrams[i], secondStationTrams[j], intersectStation, firstLength, secondLength])
        if len(trams) != 0:
            return trams
        else:
            return None

def printHelp():
    print('Для старту введіть одну з перелічених команд\n'+
          '\t 1. stop - Зупинка виконання.\n'+
          '\t 2. get_route:<route number> - Пошук маршруту за номером трамвая.\n'+
          '\t 3) station:<station name> - Знаходження маршрутів, які проїжджають крізь задану зупинку.\n'+
          '\t 4) intersect:<first route number>:<second route number> - Знаходження зупинки на яких трамваї перетинаються.\n'+
          '\t 5) length:<first station name>:<second station name> - Знаходження мінімального шляху між зупинками, якщо вони знаходяться на одному маршруті.\n'+
          '\t 6) find_route:<first station name>:<second station name>  - Знаходження якими трамваями можна доїхати з однієї зупинки до іншої (можлива одна пересадка).\n'+
          '\n')