
'''1. Реализовать функцию которая отфильтрует все буквы в строке, которые встречаются более одного раза (> 1). Пример: 
    => "agcdcgia" "agc"'''


s = "agcdcgia"

def filter_letters(s):
    result = set()
    for i in s:
        if s.count(i) > 1:            
            result.add(i)
    return ''.join(result)

# print(filter_letters(s))


'''2. Необходимо нормализовать строку убрав все дополнительные символы возле слов. Пример: 
    => normalize("X > %Y") "X > Y"
    => normalize(" X > Y <") "X > Y"
    => normalize(""X" > 'Y'> I \t> 1Z2") "X > Y > I > 1Z2"
    Дополнительные символы: !"$%&'*+,-./:;<=?[\]^`{|}~\t\n\x0b\x0c\r'''


s = ("X > %Y")
s = (" X > Y <")  # if delete second symbol '>' code will working
s = """(""X" >' Y' > I \t > 1Z2")"""

characters = """!"$%&'*+,-./:;<=?[\]^`{|}~\t\n\x0b\x0c\r""" # if delete symbol '>' code will working
result = ""

for i in s:
    if i not in characters:
        result += i
# print(result)


"""3. Преобразовать структуру списка списков в словарь. Пример:
    => toHash([["x", "y"], ["a", "b"], ["i", "j"]]) {x: "y", a: "b", i: "j"}"""

lst = ([["x", "y"], ["a", "b"], ["i", "j"]])
dct = {}

for i in lst:
    dct[i[0]] = i[1]

# print(dct)


"""4. Написать функцию которая на вход принимает объект и список ключей, а на выход отдает новый объект из полученных ключей и значений. 
    Условие: входящий объект не должен измениться.
    => select_keys({'a': 1, 'b': 2}, ['b']) {'b': 2}
    => select_keys({'a': 1, 'b': 2, 'c': 3, 'i': 4}, ['a', 'c']) {'a': 1, 'c': 3}"""

a = {'a': 1, 'b': 2}
b = ['b']

a = {'a': 1, 'b': 2, 'c': 3, 'i': 4}
b = ['a', 'c']

def object_list(a, b):
    new = {}
    for i in a.items():
        if i[0] in b:
            new[i[0]] = i[1]
    return new

# print(object_list(a, b))


"""5. Написать свою функцию, которая преобразует словарь в список списков. Пример: 
    => toArray({"0": "a", "1": "b", "2": "c"}) [["0", "a"], ["1", "b"], ["2", "c"]]"""


dct = ({"0": "a", "1": "b", "2": "c"})

def dictionary_list(dct):
    lst = []
    for i in dct.items():
        lst.append(list(i))
    return lst

# print(dictionary_list(dct))
