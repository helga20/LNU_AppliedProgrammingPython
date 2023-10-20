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
    Ідея програми полягає у тому, щоб знайти всі пари відкриваючих і закриваючих дужок у виразі, враховуючи правильне вкладення дужок.
    Алгоритм розв'язку використовує стек (Stack), в якому зберігаються позиції відкриваючих дужок. 
    Проходячи вхідний рядок (formula), програма шукає відкриваючі дужки та відповідні закриваючі дужки. 
    Кожна знайдена пара додається до списку pairs.

    Алгоритм розв'язку такий:

    Ініціалізуємо порожній стек stack і порожній список pairs для збереження пар дужок.
    Проходимося по кожному символу у вхідному рядку formula.
    Якщо це відкриваюча дужка (символ '('), то додаємо поточну позицію символу до стеку stack.
    Якщо це закриваюча дужка (символ ')'), то витягаємо останню позицію відкриваючої дужки зі стеку (якщо стек не порожній), 
    і додаємо пару позицій відкриваючої і закриваючої дужок до списку pairs.
    Повертаємо список pairs, який містить пари позицій відкриваючих і закриваючих дужок.
"""

def getParenthesesPairs(formula: str) -> list:
    stack = Stack()
    pairs = []
    for i in range(len(formula)):
        if formula[i] == '(':
            stack.push(i)
        elif formula[i] == ')':
            j = stack.pop()
            pairs.append((j, i))
    return pairs


def printPairs(pairs: list):
    for pair in pairs:
        print(f"{pair[0]} - {pair[1]}")

def printHelp():
    print(
        'Доступні команди:\n'
        '\t formula \t Ввести формулу вручну\n'

        '\t test1 \t \t (2 + 2)\n'
        '   \t \t \t 0.....6\n'

        '\t test2 \t \t (2 * (2 + 2))\n'
        '   \t \t \t 0....5....11.12\n'

        '\t test3 \t \t 3 * ( (3 + 5) + (2 + 7) + 4 * (2 * (3 - 5) + 5 * (5 + 7) ) )\n'
        '   \t \t \t ....4.6....12..16....22......30...35....41......49....55.57.59\n'

        '\t test4 \t \t 2 + 2\n'
        '   \t \t \t .....\n'

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
                formula = "(2 + 2)"

            elif command == 'test2':
                formula = '(2 * (2 + 2))'

            elif command == 'test3':
                formula = ("3 * ( (3 + 5) + (2 + 7) + "
                           "4 * (2 * (3 - 5) + 5 * (5 + 7) ) )")

            elif command == 'test4':
                formula = '2 + 2'

            else:
                print(f'Невідома команда: {command}')
                continue

            pairs = getParenthesesPairs(formula)
            if pairs:
                printPairs(pairs)
                print("Відсортовано за відкриваючими дужками:")
                printPairs(sorted(pairs, key=lambda x: x[0]))
                print("Відсортовано за закриваючими дужками:")
                printPairs(sorted(pairs, key=lambda x: x[1]))
            else:
                print("Немає дужок")

if __name__ == '__main__':
    main()
