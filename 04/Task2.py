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
    Основна ідея цієї програми полягає в тому, щоб перевірити правильність розташування дужок у математичних виразах, 
    використовуючи стек для відслідковування відкриваючих і закриваючих дужок. 
    Програма також перевіряє правильність розташування операторів і операндів.

    Алгоритм розв'язку такий:

    Визначаємо множини left_par, right_par, match_par, operands та operators для зручної перевірки типів символів у формулах.

    Функція checkFormula(formula: str) -> bool приймає рядок formula, який представляє математичний вираз.

    Використовуємо стек для перевірки розташування дужок та операторів у формулі:

    Під час проходження кожного символу у формулі:
    Якщо символ - це відкриваюча дужка (парна: "(", "[", або "{"), то додаємо її до стеку.
    Якщо символ - це операнд (наприклад, "x", "y", "z"), то додаємо спеціальне позначення "F" (яке вказує на операнд) до стеку.
    Якщо символ - це оператор (наприклад, "+", "-"), то додаємо його до стеку.
    Якщо символ - це закриваюча дужка (парна: ")", "]", або "}"), то перевіряємо правильність розташування:
    Спочатку перевіряємо, що на вершині стеку знаходиться операнд "F", оскільки закриваюча дужка повинна мати відкриваючу дужку перед собою.
    Далі перевіряємо, що наступний символ в стеці є відкриваючою дужкою, яка відповідає поточній закриваючій дужці.
    Якщо так, то видаляємо відкриваючу дужку зі стеку та додаємо "F" для позначення "закритого" виразу.
    Якщо операції виконуються правильно, продовжуємо далі.
    Після закінчення перевірки усіх символів у формулі, перевіряємо, що стек порожній. 
    Це необхідно для перевірки того, що весь вираз правильно закритий, тобто всі дужки відкриваються і закриваються коректно.
    Якщо всі перевірки пройдені успішно, повертаємо True, що означає, що формула є правильною з точки зору розташування дужок і операторів. 
    У протилежному випадку повертаємо False.
"""

left_par = {'(', '[', '{'}
right_par = {')', ']', '}'}
match_par = {')': '(', ']': '[', '}': '{'}
operands = {'x', 'y', 'z'}
operators = {'+', '-'}


def checkFormula(formula: str) -> bool:
    stack = Stack()

    for char in formula:
        if char in left_par:
            stack.push(char)
        elif char in operands:
            # позначимо операнди як F
            stack.push('F')
        elif char in operators:
            stack.push(char)
        elif char in right_par:
            while True:           
                # значення на вершині стеку перед закриваючою дужкою завжди має бути F (тобто операндом)
                rhs = stack.pop()
                if rhs != 'F':
                    return False
                
                # наступне значення має бути або оператором, або відповідною відкриваючою дужкою 
                # (в такому випадку останній операнд має бути повернутий в стек, а цикл зупинений)
                op = stack.pop()
                if op == match_par[char]:
                    stack.push('F')
                    break
                elif op not in operators:
                    return False
                
                # якщо останнє видобуте значення є оператором, то має бути ще один операнд
                lhs = stack.pop()
                if lhs != 'F':
                    return False
                
                # якщо всі попередні кроки були успішними, надіслати результат обчислення (який також є операндом) у стек
                stack.push('F')

    # виконувати такі кроки, як описано вище, доки стек не буде порожнім, 
    # який потрібен для перевірки того, що залишилося після обробки всіх дужок
    while not stack.empty():
        rhs = stack.pop()
        if rhs != 'F':
            return False
        if stack.empty():
            break
        op = stack.pop()
        if op not in operators:
            return False
        lhs = stack.pop()
        if lhs != 'F':
            return False
        stack.push('F')

    return True

def printHelp():
    print(
        'Доступні команди:\n'
        '\t formula \t Ввести формулу вручну\n'

        '\t test1 \t \t x + ( y - z - [ x + x ] + { [ z - z - y ] + ( y ) } ) - z\n'
        '   \t \t \t Очікується True\n'

        '\t test2 \t \t {(x)}\n'
        '   \t \t \t Очікується True\n'

        '\t test3 \t \t x + y + z\n'
        '   \t \t \t Очікується True\n'

        '\t test4 \t \t x + (x - (y + z)\n'
        '   \t \t \t Очікується False\n'

        '\t test5 \t \t + x \n'
        '   \t \t \t Очікується False\n'

        '\t test6 \t \t x + (y + z}\n'
        '   \t \t \t Очікується False\n'

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
                formula = \
                    'x + ( y - z - [ x + x ] + { [ z - z - y ] + ( y ) } ) - z'

            elif command == 'test2':
                formula = '{(x)}'

            elif command == 'test3':
                formula = 'x + y + z'

            elif command == 'test4':
                formula = 'x + (x - (y + z)'

            elif command == 'test5':
                formula = '+ x'

            elif command == 'test6':
                formula = 'x + (y + z}'

            else:
                print(f'Невідома команда: {command}')
                continue

            result = checkFormula(formula)
            print(result)

if __name__ == '__main__':
    main()
