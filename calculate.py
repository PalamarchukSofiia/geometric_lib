import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
    "perimeter-triangle": 3,
    "area-triangle": 3,
}

# Создаем словарь для безопасного вызова функций
function_mapping = {
    'circle': {
        'perimeter': circle.perimeter,
        'area': circle.area
    },
    'square': {
        'perimeter': square.perimeter,
        'area': square.area
    },
    'triangle': {
        'perimeter': triangle.perimeter,
        'area': triangle.area
    }
}

def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Figure {fig} is not supported. Available figures: {figs}")
    if func not in funcs:
        raise ValueError(f"Function {func} is not supported. Available functions: {funcs}")

    expected_size = sizes.get(f"{func}-{fig}", 1)
    if len(size) != expected_size:
        raise ValueError(f"Invalid number of sizes for {fig} {func}: expected {expected_size}, got {len(size)}")

    try:
        # Безопасный вызов функции через словарь
        result = function_mapping[fig][func](*size)
    except Exception as e:
        raise e

    # Форматирование результата
    if fig == 'circle':
        if func == 'perimeter':
            operation_str = f"Perimeter of {fig} ({size[0]}) = {result:.2f}"
        elif func == 'area':
            operation_str = f"Area of {fig} (π * {size[0]}^2) = {result:.2f}"
    elif fig == 'square':
        if func == 'perimeter':
            operation_str = f"Perimeter of {fig} ({size[0]}) = {result}"
        elif func == 'area':
            operation_str = f"Area of {fig} ({size[0]} * {size[0]}) = {result}"
    elif fig == 'triangle':
        if func == 'perimeter':
            operation_str = f"Perimeter of {fig} ({' + '.join(map(str, size))}) = {result}"
        elif func == 'area':
            operation_str = f"Area of {fig} (Heron's formula for sides {size[0]}, {size[1]}, {size[2]}) = {result:.2f}"
    else:
        operation_str = f"{func.capitalize()} of {fig} with size {', '.join(map(str, size))} = {result}"

    return operation_str

if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n").strip().lower()

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n").strip().lower()

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        try:
            size_input = input("Input figure sizes separated by space: ").strip()
            size = list(map(float, size_input.split()))
        except ValueError:
            print("Please enter valid numbers.")

    operation_str = calc(fig, func, size)
    print(operation_str)

