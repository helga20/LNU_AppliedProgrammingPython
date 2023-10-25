import http.client
import sys
import os

def get(server, url):
    # надсилання запиту на отримання за певною URL-адресою
    try:
        server.request('GET', url) # відправлення запиту на отримання
        response = server.getresponse() # отримання відповідь від сервера
    except:
        info = sys.exc_info() # отримання помилки
        print(info[0], info[1]) # запис помилки в консоль
        return
    return response # повернення відповіді сервера

def getAndWriteToFile(server, url, filename):
     # надсилання запиту на отримання за певною URL-адресою та запис у файл
    response = get(server, url) # відправлення запиту на отримання
    if response is None:
        print("Error occurred while sending request") # друк помилки, якщо відповідь порожня
    elif response.status == 200:
        with open(filename, "wb") as file: # відкриття файлу для запису
            file.write(response.read()) # запис у файл
        response.close()
    else:
        print("Error occurred while sending request", response.status, response.reason) # показ помилки сервера

def openFile(filename):
     # відкриття файл програмою, встановленою за замовчуванням
    path = os.path.join(os.path.abspath("."), filename) # отримання поточної папки
    os.startfile(path) # запуск файлу за допомогою програми за замовчуванням

def main():
    print("Loading...")
    server = http.client.HTTPSConnection("uk.wikipedia.org") # створення примірника клієнта http
    filename = "test.html"
    getAndWriteToFile(server, "/wiki/Python", filename) #отримання відповіді і запис її у файл
    openFile(filename) # відкриття файлу
    
if __name__ == "__main__":
    main()
