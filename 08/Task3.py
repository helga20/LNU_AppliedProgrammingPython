import urllib.request
import os

def main():
    print("Loading...")
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    filename = "test_xmlResult.xml"
    xmlFile = urllib.request.urlopen(url) # отримання xml файлу
    with open(filename, "wb") as file: # відкриття файлу
        file.write(xmlFile.read()) # запис файлу
    xmlFile.close() # закриття файлу
    path = os.path.join(os.path.abspath("."), filename) # отримання шляху до файлу
    os.startfile(path) # запуск файлу за допомогою програми за замовчуванням

if __name__ == "__main__":
    main()
