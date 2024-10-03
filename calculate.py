# Импортируем модули для работы с кругом и квадратом
import circle
import square

# Список допустимых фигур
figs = ['circle', 'square']

# Список допустимых функций
funcs = ['perimeter', 'area']

# Словарь для хранения размеров фигур
sizes = {}

# Функция для вычисления периметра или площади фигуры
def calc(fig, func, size):

        # Проверяем, что введенная фигура допустима
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')# Вычисляем результат
	print(f'{func} of {fig} is {result}')# Выводим результат на экран


# Основная часть программы
if __name__ == "__main__":
        # Инициализируем переменные для ввода данных
	func = ''
	fig = ''
	size = list()

        # Вводим название фигуры до тех пор, пока не будет введено допустимое значение
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

	# Вызываем функцию для вычисления результата
	calc(fig, func, size)



