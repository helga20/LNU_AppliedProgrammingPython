import TramSchedulesLvivUI as trFunc
import tkinter as tk
from tkinter import ttk

def main():

    root = tk.Tk()
    root.title("Програма пошуку маршруту")
    root.geometry("1000x450")
    root.config(bg='#006992')

    mainLabel = ttk.Label(root, 
                        text="Ви хочете дізнатись як потрапити з однієї зупинки трамвая до іншої ? \n              Виберіть зі списку назви трамвайних зупинок", 
                        width=60,
                        anchor="n", 
                        font=("Arial", 16), 
                        foreground='white', 
                        background='#006992')
    mainLabel.grid(row=0, column=0, columnspan=2, pady=20)

    labelFrom = ttk.Label(root, 
                        text="Звідки їхати:", 
                        width=20, 
                        anchor="w", 
                        font=("Arial", 12), 
                        foreground='white', 
                        background='#006992')
    labelFrom.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    labelTo = ttk.Label(root, 
                        text="Куди їхати:", 
                        width=20, 
                        anchor="w", 
                        font=("Arial", 12), 
                        foreground='white', 
                        background='#006992')
    labelTo.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    numbersT = trFunc.getData('routes.txt')
    streets = []
    for key in numbersT:
        for key2 in numbersT[key]:
            for i in numbersT[key][key2]:
                if i not in streets:
                    streets.append(i)

    comboFrom = ttk.Combobox(root, 
                            values=streets, 
                            width=50, 
                            font=("Arial", 12))
    comboFrom.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    comboTo = ttk.Combobox(root,
                        values=streets, 
                        width=50, 
                        font=("Arial", 12))
    comboTo.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    result = tk.Text(root, 
                    width=100, 
                    height=8, 
                    font=("Arial", 12))
    result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def findRoute():
        result.delete(1.0, tk.END)
        route = trFunc.getRoute(numbersT, comboFrom.get(), comboTo.get())
        if route is not None:
            if comboFrom.get() == '' or comboTo.get() == '':
                result.insert(1.0, "Ви не вибрали зупинку")
                return
            if type(route[0]) == int:
                result.insert(1.0, f'Зі станції "{comboFrom.get()}" до стандії "{comboTo.get()}" можна добратися трамваєм №{route[1]} (к-сть зупинок {route[0]})') 
            else:
                for variant in route:                  
                    result.insert(tk.END, f'{route.index(variant) + 1}) Щоб добратися зі станції "{comboFrom.get()}" до стандії "{comboTo.get()}" необхідно спочатку сісти на трамвай №{variant[0]} '+
                            f'(к-сть зупинок {variant[3]}), а потім пересісти на трамвай №{variant[1]} на зупинці "{variant[2]}" (к-сть зупинок {variant[4]})\n')
        else:
            result.insert(1.0, "Скористайтесь іншим видом транспорту")

    button = ttk.Button(root,
                        text="Знайти маршрут",
                        width=20,
                        command=findRoute)
    button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



    root.mainloop()

if __name__ == "__main__":
    main()