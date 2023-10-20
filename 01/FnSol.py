import os

def FnSol1(filename):
    pos_num_amount = 0
    neg_num_amount = 0
    neg_num_average = 0

    try:
        with open(filename, 'r') as values:
            for val in values:
                numbers = val.strip().split()
                for num in numbers:
                    num = int(num)
                    if num > 0:
                        pos_num_amount += 1
                    elif num < 0:
                        neg_num_amount += 1
                        neg_num_average += num
        
        neg_num_average = neg_num_average / neg_num_amount if neg_num_amount != 0 else 0

        return pos_num_amount, neg_num_amount, neg_num_average
    
    except FileNotFoundError:
        return None

def FnSol2(filename):
    try:
        with open(filename, 'r') as values:
            lines = values.readlines()
            if len(lines) >= 3:
                a = float(lines[0])
                b = float(lines[1])
                c = float(lines[2])
                
                if a <= 0 or b <= 0 or c <= 0:
                    return "Не можна утворити трикутник"

                if a + b > c and a + c > b and b + c > a:
                    if a == b == c:
                        return "Рівносторонній трикутник"
                    elif a == b or a == c or b == c:
                        return "Рівнобедрений трикутник"
                    else:
                        return "Різносторонній трикутник"
                else:
                    return "Не можна утворити трикутник"
            
    except FileNotFoundError:
        return None

def FnSol3(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as values:
            input_string = values.read()
            words = input_string.split()
            result = os.linesep.join(words)
            return result
        
    except FileNotFoundError:
        return None

def FnSol4(filename):
    try:
        with open(filename, 'r') as file:
            arr = []
            lines = file.readlines()
            for line in lines:
                row = list(map(int, line.split()))
                arr.append(row)

            if not arr:
                return 0

            max_sum = float('-inf')
            rows, cols = len(arr), len(arr[0])
            left = right = top = bottom = 0

            for i in range(rows):
                for j in range(cols):
                    for k in range(i, rows):
                        for l in range(i, cols):
                            cur_sum = sum(arr[x][y] for x in range(i, k + 1) for y in range(j, l + 1))
                            if cur_sum > max_sum:
                                max_sum = cur_sum
                                left, right, top, bottom = j, l, i, k
            return max_sum, (left, right, top, bottom)
        
    except FileNotFoundError:
        return None

def Testorg():

    while True:
        print("Виберіть номер задачі (1-4); e - вихід:")
        choice = input()
        if choice == 'e':
            break
        elif choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= 4:
                list_results = []

                if choice == 1:
                    list_results.clear()
                    with open('InData1.txt', 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        list_input_data = list(map(int, line.split()))
                    list_results.append(FnSol1('InData1.txt'))  
                    with open('ResultAll.txt', 'a', encoding='utf-8') as file:
                        result = 'Задача 1: \nВхідні дані: \n' + '\n'.join(str(item) for item in lines) + '\nОтримані результати: \n' + '\n'.join(str(item) for item in list_results) + '\n'
                        file.write(str(result))

                elif choice == 2:
                    list_results.clear()
                    with open('InData2.txt', 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        list_input_data = list(map(int, line.split()))
                        list_results.append(FnSol2('InData2.txt'))
                    with open('ResultAll.txt', 'a', encoding='utf-8') as file:
                        result = 'Задача 2: \nВхідні дані: \n' + ''.join(str(item) for item in lines) + '\nОтримані результати: \n' + '\n'.join(str(item) for item in list_results) + '\n'
                        file.write(str(result))  

                elif choice == 3:
                    list_results.clear()
                    with open('InData3.txt', 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                    for line in lines:
                        list_input_data = list(map(str, line.split()))
                        list_results.append(FnSol3('InData3.txt'))
                    with open('ResultAll.txt', 'a', encoding='utf-8') as file:
                        result = 'Задача 3: \nВхідні дані: \n' + ''.join(str(item) for item in lines) + '\nОтримані результати: \n' + '\n'.join(str(item) for item in list_results) + '\n'
                        file.write(str(result))  

                elif choice == 4:
                    list_results.clear()
                    with open('InData4.txt', 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        list_input_data = list(map(int, line.split()))
                        list_results.append(FnSol4('InData4.txt'))
                    with open('ResultAll.txt', 'a', encoding='utf-8') as file:
                        result = 'Задача 4: \nВхідні дані: \n' + ''.join(str(item) for item in lines) + '\nОтримані результати: \n' + '\n'.join(str(item) for item in list_results) + '\n'
                        file.write(str(result))

                else:
                    print("Не знайдено вхідних даних.")
            else:
                print("Неправильний номер задачі. Виберіть цифру від 1 до 4.")
        else:
            print("Неправильний ввід.")           

if __name__ == "__main__":
    Testorg()