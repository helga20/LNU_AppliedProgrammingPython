import datetime

class Queue:
    def __init__(self):
        self.queue = []

    def createFromList(self, newQueue):
        self.queue = newQueue
        
    def __str__(self):
        return "<back> [" + ",".join(map(str, self.queue)) + "] <front>"
    
    def into(self, obj):
        self.queue.insert(0, obj)
        return self
    
    def take(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None
        
    def __len__(self):
        return len(self.queue)
    
    def front(self):
        if self.queue:
            return self.queue[len(self.queue) - 1]
        else:
            return None
        
    def back(self):
        if self.queue:
            return self.queue[0]
        else:
            return None
        
    def empty(self):
        return not self.queue
    
    def clear(self):
        self.queue = []
        
    def find(self, key = lambda x : True):
        try:
            indexList = [i for i in range(len(self.queue)) if key(self.queue[i])]
            return indexList
        except:
            return []
        pass
    
    def remove(self, k):
        if 0 <= k < len(self.queue):
            y = self.queue[k]
            del self.queue[k: k + 1]
            return y
        else:
            return None
        
    def all(self):
        return self.queue

class Border:

    def __init__(self, queue):
        self.general = queue

    def divideIntoQueues(self):

        """"
        Розподіл на дві черги. Якщо загальна ціна товару автомобіля < 30000, він може перейти на зелений шлях.
        """

        withDeclaration = Queue()
        greenPath = Queue()

        while(len(self.general) > 0):
            car = self.general.take()
            if car['amount'] * car['price'] < 30000:
                greenPath.into(car)
            else:
                withDeclaration.into(car)

        return withDeclaration, greenPath
        
    def filterCars(self, queue, key, value):

        """
        Фільтрація автомобілів за певним ключем і його значенням.
        """

        if key == 'from' or key == 'to':
            indexes = queue.find(lambda x : value in x[key])
        else:        
            indexes = queue.find(lambda x : x[key] == value)
        return indexes
    
    def removeCarsFromRussia(self): 

        """
        Впускати в країну автомобілі з росії заборонено!
        """

        indexes = self.filterCars(self.general, 'from', 'Росія')

        if len(indexes) != 0:
            deletedCount = 0
            for i in indexes:
                self.general.remove(i - deletedCount)
                deletedCount += 1
                print(f'Автомобіль #{i} було вилучено з черги тому, що він з росії')
        else:
            print('Це не автомобіль з росії')

    def removeCarsFromBelarus(self): 

        """
        Впускати в країну автомобілі з білорусі небезпечно!
        """

        indexes = self.filterCars(self.general, 'from', 'Білорусь')

        if len(indexes) != 0:
            deletedCount = 0
            for i in indexes:
                self.general.remove(i - deletedCount)
                deletedCount += 1
                print(f'Автомобіль #{i} було вилучено з черги тому, що він з білорусі')
        else:
            print('Це не автомобіль з білорусі')  

    def crossBorder(self, queue):

        """
        Перетин кордону автомобілем
        """

        goodsList = []
        carWithMaxTotalPrice = queue.front()
        maxTotalPrice = carWithMaxTotalPrice['price'] * carWithMaxTotalPrice['amount']   

        while(len(queue) > 0):
            car = queue.take()
            if(car['withCarriageContract'] == True):
                model = car['model']
                number = car['number']
                goods = car['goods']
                amount = car['amount']
                price = car['price']  
                isInGoodsList = False

                total_price = price * amount
                if total_price > maxTotalPrice:
                    carWithMaxTotalPrice = car
                    maxTotalPrice = total_price

                for st in goodsList:
                    if(st['goods'] == goods):
                        isInGoodsList = True
                        st['amount'] += amount
                        st['total price'] += price * amount
                        break
                if(isInGoodsList == False):         
                    goodsList.append({'goods' : goods, 'price' : price, 'amount' : amount, 'total price' : total_price})
                print(f'\t{model} ({number}) перетнув кордон з країною')            
            else:
                model = car['model']
                number = car['number']
                print(f'\t{model} ({number}) не був пропущений через кордон з країною, оскільки не мав договору перевезення')

        return goodsList, carWithMaxTotalPrice, maxTotalPrice
    
def printStatistics(statistic):
    
    """
    Виведення на консоль статистики
    """

    print(f'\t{statistic["goods"]}: Загальна кількість = {statistic["amount"]}, Загальна сума = {statistic["total price"]}')

def printCar(car):

    """
    Виведення на консоль автомобілів
    """

    print(f'{car["model"]} ({car["number"]}):')
    print(f'\t Компанія: {car["company"]}')
    print(f'\t Дата: {car["date"]}')
    print(f'\t Звідки: {car["from"][0]}, {car["from"][1]}')
    print(f'\t Куди: {car["to"][0]}, {car["to"][1]}')
    print(f'\t Товари: {car["goods"]}')
    print(f'\t Вартість одного товару: {car["price"]}')
    print(f'\t Кількість: {car["amount"]}')
    print(f'\t З договором перевезення: {"Так" if car["withCarriageContract"] else "Ні" }')

def main():

    # Ініціалізація загальної черги перед поділом на «зелену чергу» і не «зелену чергу»

    initialQueue = Queue()
    initialQueue.createFromList([
        {
            'model':'BMW',
            'number':'BC 1823 АТ',
            'company':'Huawei',
            'date': datetime.datetime.strptime('04.10.2023', '%d.%m.%Y'),
            'from':('Польща','Краків'),
            'to':('Україна','Львів'),
            'goods':'телефон',
            'price':2500,
            'amount':5,
            'withCarriageContract':True
        },
        {
            'model':'Лада',
            'number':'к213нр',
            'company':'LG',
            'date': datetime.datetime.strptime('02.10.2023', '%d.%m.%Y'),
            'from':('Росія', 'Москва'),
            'to':('Україна','Київ'),
            'goods':'ноутбук',
            'price':4500,
            'amount':5,
            'withCarriageContract':True
        },
        {
            'model':'BMW',
            'number':'XP 584NK',
            'company':'BetterSilver',
            'date': datetime.datetime.strptime('23.09.2023', '%d.%m.%Y'),
            'from':('Італія','Венеція'),
            'to':('Україна','Житомир'),
            'goods':'прикраса',
            'price':3000,
            'amount':5,
            'withCarriageContract':False
        },
        {
            'model':'Unison',
            'number':'0126 АВ-6',
            'company':'Samsung',
            'date': datetime.datetime.strptime('03.10.2023', '%d.%m.%Y'),
            'from':('Білорусь', 'Мінськ'),
            'to':('Україна','Київ'),
            'goods':'мікрохвильовка',
            'price':2500,
            'amount':10,
            'withCarriageContract':True
        },
        {
            'model':'Volvo',
            'number':'RD ZS 120',
            'company':'Рошен',
            'date': datetime.datetime.strptime('01.10.2023', '%d.%m.%Y'),
            'from':('Німеччина','Гамбург'),
            'to':('Україна','Ужгород'),
            'goods':'солодощі',
            'price':100,
            'amount':12,
            'withCarriageContract':False
        },
        {
            'model':'Nissan',
            'number':'CZ 007NF',
            'company':'SilverLine',
            'date': datetime.datetime.strptime('29.09.2023', '%d.%m.%Y'),
            'from':('Італія','Мілан'),
            'to':('Україна','Чернівці'),
            'goods':'прикраса',
            'price':10000,
            'amount':8,
            'withCarriageContract':True
        },
        {
            'model':'BMW',
            'number':'в587ex',
            'company':'Оленка',
            'date': datetime.datetime.strptime('03.10.2023', '%d.%m.%Y'),
            'from':('Росія', 'Новосибірськ'),
            'to':('Україна','Харків'),
            'goods':'солодощі',
            'price':90,
            'amount':100,
            'withCarriageContract':True
        },
        {
            'model':'Toyota',
            'number':'OK TE 749',
            'company':'Honor',
            'date': datetime.datetime.strptime('05.10.2023', '%d.%m.%Y'),
            'from':('Німеччина','Берлін'),
            'to':('Україна','Київ'),
            'goods':'ноутбук',
            'price':3800,
            'amount':16,
            'withCarriageContract':True
        },
        {
            'model':'Skoda',
            'number':'3R6 9710',
            'company':'KOBI',
            'date': datetime.datetime.strptime('01.10.2023', '%d.%m.%Y'),
            'from':('Чехія','Брно'),
            'to':('Україна','Херсон'),
            'goods':'прикраса',
            'price':3000,
            'amount':25,
            'withCarriageContract':True
        },
        {
            'model':'Renault',
            'number':'OKT 63RA',
            'company':'Gorenje',
            'date': datetime.datetime.strptime('15.09.2023', '%d.%m.%Y'),
            'from':('Польща','Лодзь'),
            'to':('Україна','Київ'),
            'goods':'холодильник',
            'price':15000,
            'amount':3,
            'withCarriageContract':True
        },
        {
            'model':'Audi',
            'number':'ERA 75TM',
            'company':'HP',
            'date': datetime.datetime.strptime('27.09.2023', '%d.%m.%Y'),
            'from':('Польща','Ярослав'),
            'to':('Україна','Хмельницький'),
            'goods':'ноутбук',
            'price':2500,
            'amount':2,
            'withCarriageContract':False
        },
        {
            'model':'Volvo',
            'number':'ZH 445789',
            'company':'Apple',
            'date': datetime.datetime.strptime('28.09.2023', '%d.%m.%Y'),
            'from':('Швейцарія','Цюрих'),
            'to':('Україна','Київ'),
            'goods':'телефон',
            'price':4000,
            'amount':12,
            'withCarriageContract':True
        },
        {
            'model':'Nissan',
            'number':'1A2 3000',
            'company':'Bosch',
            'date': datetime.datetime.strptime('04.10.2023', '%d.%m.%Y'),
            'from':('Чехія','Прага'),
            'to':('Україна','Черкаси'),
            'goods':'мікрохвильовка',
            'price':2600,
            'amount':1,
            'withCarriageContract':False
        },
        {
            'model':'Opel',
            'number':'PO 567841',
            'company':'Gorenje',
            'date': datetime.datetime.strptime('05.10.2023', '%d.%m.%Y'),
            'from':('Швейцарія','Женева'),
            'to':('Україна','Харків'),
            'goods':'холодильник',
            'price':6000,
            'amount':1,
            'withCarriageContract':False
        },
        {
            'model':'Неман',
            'number':'6708 PO-8',
            'company':'Samsung',
            'date': datetime.datetime.strptime('02.10.2023', '%d.%m.%Y'),
            'from':('Білорусь', 'Брест'),
            'to':('Україна','Луцьк'),
            'goods':'мікрохвильовка',
            'price':3000,
            'amount':1,
            'withCarriageContract':False
        },
        {
            'model':'Audi',
            'number':'E 77 PKW',
            'company':'Lenovo',
            'date': datetime.datetime.strptime('24.09.2023', '%d.%m.%Y'),
            'from':('Румунія','Бухарест'),
            'to':('Україна','Запоріжжя'),
            'goods':'планшет',
            'price':2300,
            'amount':15,
            'withCarriageContract':True
        }
    ])
    
    border = Border(initialQueue)
    border.removeCarsFromRussia()
    border.removeCarsFromBelarus()

    indexesInQueue = border.filterCars(initialQueue, 'goods', 'ноутбук')
    print(f'\nІндекси автомобілів з ноутбуками в початковій черзі: {indexesInQueue}')

    indexesInQueue = border.filterCars(initialQueue, 'to', 'Київ')
    print(f'\nІндекси автомобілів які прямують до Києва в початковій черзі: {indexesInQueue}')

    withDeclaration, greenPath = border.divideIntoQueues()

    print("\nАвтомобілі, які в'їхали в країну з черги з декларуванням:")
    withDeclarationStatistics, carWithMaxTotalPrice, maxTotalPrice = border.crossBorder(withDeclaration)
    print()
    for st in withDeclarationStatistics:
        printStatistics(st)
    print(f'\nАвтомобіль з найбільшою загальною ціною в черзі з декларацією: {maxTotalPrice}')
    printCar(carWithMaxTotalPrice)

    print("\nАвтомобілі, які в'їжджали в країну з зеленого коридору:")
    greenPathStatistics, carWithMaxTotalPrice, maxTotalPrice = border.crossBorder(greenPath)
    print()
    for st in greenPathStatistics:
        printStatistics(st)
    print(f'\nАвтомобіль з найбільшою загальною ціною в зеленому коридорі: {maxTotalPrice}')
    printCar(carWithMaxTotalPrice)

if __name__ == '__main__':
    main()