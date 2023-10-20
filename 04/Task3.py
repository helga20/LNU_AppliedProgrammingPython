class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def empty(self):
        return not self.stack

    def len(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()

"""
    Програма реалізує обчислення виразів, які представлені у вигляді рядка формули, що містить дві операції: 
    додавання (S) і ділення (D). Операції виконуються в межах дужок.
    Програма використовує стеки для зберігання операторів і чисел, розбирає рядок формули і виконує 
    обчислення згідно з правилами операцій.

    Алгоритм розв'язку акий:

    Створюємо два стеки: один для операторів (operators) і інший для чисел (numbers).
    Читаємо формулу посимвольно, перебираючи символи зліва направо.
    Якщо символ - це 'S' або 'D', додаємо його до стеку операторів (operators).
    Якщо символ є цифрою, зчитуємо всю послідовність цифр і додаємо її як число до стеку чисел (numbers).
    Якщо символ - це ')', витягуємо один оператор зі стеку операторів (operators) і два числа зі стеку чисел (numbers). 
    Виконуємо обчислення згідно з виділеним оператором і додаємо результат назад до стеку чисел (numbers).
    Повторювати цей процес для всієї формули.
    На завершення роботи в стеку чисел (numbers) залишиться одне число - результат обчислення всієї формули.
    Повертаємо це число як вихідний результат.
"""

def evaluate(formula: str) -> int:
    operators = Stack()
    numbers = Stack()
    i = 0

    while i < len(formula):
        char = formula[i]

        # добавляємо оператор в стек операторів
        if char == 'S' or char == 'D':
            operators.push(char)

        # добавляємо число в стек чисел 
        elif char.isdigit():
            number_start = i
            while formula[i+1].isdigit():
                i += 1
            number = formula[number_start:i+1]
            numbers.push(int(number))

        # вилучаємо зі стеку оператор і числа та виконуємо обчислення
        elif char == ')':
            op = operators.pop()
            rhs = numbers.pop()
            lhs = numbers.pop()
            if op == 'S':
                numbers.push(lhs + rhs)
            elif op == 'D':
                numbers.push(int(lhs / rhs))

        i += 1

    result = numbers.pop()
    return result

def printHelp():
    print(
        'Доступні команди:\n'
        '\t formula \t ввести формулу вручну\n'
        
        '\t test1 \t \t S(3,3)\n'
        '   \t \t \t Очікується 6\n'

        '\t test2 \t \t D(6,2)\n'
        '   \t \t \t Очікується 3\n'

        '\t test3 \t \t D(5,2)\n'
        '   \t \t \t Очікується 2\n'

        '\t test4 \t \t D(8,S(2,1))\n'
        '   \t \t \t Очікується 2\n'

        '\t test5 \t \t S(D(8,2),D(S(10,3),2))\n'
        '   \t \t \t Очікується 10\n'

        '\t test6 \t \t D(S(10,20),15)\n'
        '   \t \t \t Очікується 2\n'

        '\t exit \t \t Вихід'
    )
    

def main():
    printHelp()

    while True:
        command = input('> ')

        if command == 'exit':
            return

        elif not command:
            pass

        else:
            if command == 'formula':
                formula = input('formula> ')

            elif command == 'test1':
                formula = 'S(3,3)'

            elif command == 'test2':
                formula = 'D(6,2)'

            elif command == 'test3':
                formula = 'D(5,2)'

            elif command == 'test4':
                formula = "D(8,S(2,1))"

            elif command == 'test5':
                formula = "S(D(8,2),D(S(10,3),2))"

            elif command == 'test6':
                formula = "D(S(10,20),15)"

            else:
                print(f'Unknown command: {command}')
                continue

            result = evaluate(formula)
            print(result)

if __name__ == '__main__':
    main()
