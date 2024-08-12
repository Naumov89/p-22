"""Рівносторонній трикутника з символів * """

def print_equilateral_triangle(n):
    for i in range(n): # Цикл проходить по кожному рядку від 0 до n-1.
        spaces = ' ' * (n - i - 1) # Кількість пробілів перед зірочками зменшується з кожним рядком.
        stars = '*' * (2 * i + 1) # Кількість зірочок збільшується з кожним рядком.
        print(spaces + stars)

print_equilateral_triangle(5)

"""Перевернутий рівносторонній трикутника з символів * """ 

def print_inverted_pyramid(n):
    for i in range(n, 0, -1): # Цикл проходить по кожному рядку від n до 1 (включно).
        spaces = ' ' * (n - i) # Кількість пробілів перед зірочками збільшується з кожним рядком.
        stars = '*' * (2 * i - 1) # Кількість зірочок зменшується з кожним рядком.
        print(spaces + stars)

print_inverted_pyramid(5)

""" Перевернута піраміда, з символів *"""

def print_right_aligned_pyramid(n):
    for i in range(n, 0, -1): # Цикл проходить по кожному рядку від n до 1 (включно).
        stars = '*' * (2 * i - 1) # Кількість зірочок зменшується з кожним рядком.
        print(stars)

print_right_aligned_pyramid(5)

"""Піраміда з символів *:"""
def print_pyramid(n):
    for i in range(1, n + 1): # Цикл проходить по кожному рядку від 1 до n (включно).
        stars = '*' * (2 * i - 1) # Кількість зірочок збільшується з кожним рядком.
        print(stars)

print_pyramid(5)


