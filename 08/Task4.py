import xml.etree.ElementTree as ET

def parse_currency_exchange_xml(filename):
    tree = ET.parse(filename) # отримання xml файлу
    root = tree.getroot() # отримання кореневого (головного) елемента xml файлу 

    # Функція для отримання інформації про валюту за її кодом
    def get_currency_info(currency_code): 
        for currency in root.findall('currency'): # отримання всіх елементів списку currency
            cc = currency.find('cc').text # отримання коду валюти з поточного елемента
            if cc == currency_code: # перевірка, чи співпадає код валюти з переданим
                # отримання решти інформації про валюту
                r030 = currency.find('r030').text # ідентифікатор валюти
                txt = currency.find('txt').text # назва валюти
                rate = currency.find('rate').text # обмінний курс валюти
                exchangedate = currency.find('exchangedate').text # дата останнього обміну
                # повернення інформації про валюту у вигляді словника
                return {
                    'Currency ID': r030,
                    'Currency Name': txt,
                    'Exchange Rate': rate,
                    'Currency Code': cc,
                    'Exchange Date': exchangedate
                }
        return None # якщо жодна валюта не відповідає переданому коду, повертаємо None

    # Функція для знаходження середнього обмінного курсу для певної валюти
    def find_average_exchange_rate(currency_code): 
        total_rate = 0
        count = 0
        for currency in root.findall('currency'):
            cc = currency.find('cc').text # отримання коду валюти з поточного елемента
            if cc == currency_code: # перевірка, чи співпадає код валюти з переданим
                rate = float(currency.find('rate').text)  # отримання обмінного курсу
                total_rate += rate 
                count += 1
        if count > 0:
            return total_rate / count # якщо знайдено хоча б одну валюту з переданим кодом, обчислюємо середній обмінний курс
        return None # якщо жодна валюта не відповідає переданому коду, повертаємо None

    # Функція для знаходження валюти з найвищим обмінним курсом
    def find_highest_exchange_rate_currency():
        max_rate = 0
        currency_info = None
        for currency in root.findall('currency'):  
            rate = float(currency.find('rate').text) # отримання обмінного курсу для поточної валюти
            if rate > max_rate: # перевірка, чи обмінний курс більший за максимальний знайдений обмінний курс
                max_rate = rate # оновлення максимального обмінного курсу
                currency_info = {
                    'Currency ID': currency.find('r030').text,
                    'Currency Name': currency.find('txt').text,
                    'Exchange Rate': currency.find('rate').text,
                    'Currency Code': currency.find('cc').text,
                    'Exchange Date': currency.find('exchangedate').text
                }
        return currency_info # повернення інформації про валюту з найвищим обмінним курсом або None, якщо немає жодної валюти

    # Виведення інформації про певну валюту (USD, наприклад)
    usd_info = get_currency_info('USD')
    if usd_info:
        print("Інформація про USD:")
        for key, value in usd_info.items():  
            print(f"{key}: {value}") # виведення параметру валюти та відповідного значення
        print("\n")

    # Знаходження середнього обмінного курсу для EUR
    average_eur_rate = find_average_exchange_rate('EUR')
    if average_eur_rate is not None:
        print(f"Середній курс обміну EUR: {average_eur_rate}\n") # виведення середнього обмінного курсу для EUR

    # Знаходження валюти з найвищим обмінним курсом
    highest_rate_currency = find_highest_exchange_rate_currency()
    if highest_rate_currency:
        print("Валюта з найвищим курсом:")
        for key, value in highest_rate_currency.items():  
            print(f"{key}: {value}") # виведення інформації про валюту з найвищим обмінним курсом

def main():
    parse_currency_exchange_xml('test_xmlResult.xml')

if __name__ == "__main__":
    main()
