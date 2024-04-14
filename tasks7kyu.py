###1
"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""

# def find_short(s):
#     l = s.split(' ')
#     result = min(len(i) for i in l)
#     return result

# def find_short(s):
#     return min(len(x) for x in s.split())

###2
"""Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"""

# def maskify(cc):
#     len_cc = len(cc)
#     four_cc = cc[-4:]
#     print(four_cc)
#     if len(cc) <= 4:
#         return cc
#     else:
#         return (len_cc - 4) * "#" + four_cc
    
# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]

# print(maskify('SF$SDfgsd2eA'))

###3
"""Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)"""

# def get_sum(a,b):
   
   
   
   
   
###4
"""DESCRIPTION:
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e."""


# def friend(x):
#     rezult = [name for name in x if len(name) == 4]
#     return rezult

###5
"""Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"""

# def longest(a1, a2):
#     suma = set(a1 + a2)
#     suma2 = sorted(suma)
#     return "".join(suma2)

# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))

###6
"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false"""

# def validate_pin(pin):
#     result =(len(pin) == 4 or len(pin) == 6) and all(i.isdigit() for i in pin)
#     return result

# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()

###6
"""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)"""

# def add_binary(a, b):
#     c = a + b
#     return bin(c)[2:]

# def add_binary(a,b):
#     return bin(a+b)[2:]

###7
"""Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false"""

# def solution(text, ending):
#     return text.endswith(ending)


###7

"""Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11"""

def binary_array_to_number(arr):
    return int("".join(str(i) for i in arr),2)

###8

"""There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop."""

def number(bus_stops):
    even_numbers = [stop[0] for stop in bus_stops]
    odd_numbers = [stop[1] for stop in bus_stops]
    sum_even = sum(even_numbers)
    sum_odd = sum(odd_numbers)
    return sum_even - sum_odd

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum

###9

"""Task:
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"""

def odd_or_even(arr):
    sum_arr = sum(arr)
    if sum_arr % 2 != 0:
        return "odd"
    else:
        return "even"


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

###10

"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"""

def reverse_words(text):
    words = text.split(" ")
    new_words = [word[::-1] for word in words]
    return " ".join(new_words)

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

###11

"""The museum of incredibly dull things
The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]"""

def remove_smallest(numbers):
    if not numbers:
        return []
    min_numbers = numbers.index(min(numbers))
    result = numbers[:min_numbers] + numbers[min_numbers + 1:]
    return result

def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

###12

"""Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]"""

def number(lines):
    result = [f"{ind}: {num}" for ind, num in enumerate(lines, 1)]
    return result

def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

###13

"""Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.

Examples (Input --> Output)
[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]"""

def min_max(lst):
    min_lst =  min(lst)
    max_lst = max(lst)
    result = [min_lst, max_lst]
    return result

def min_max(lst):
    return [min(lst), max(lst)]

###13

"""Don't give me five!
In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
The result may contain fives. ;-)
The start number will always be smaller than the end number. Both numbers can be also negative!

I'm very curious for your solutions and the way you solve it. Maybe someone of you will find an easy pure mathematics solution.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!"""

def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        if '5' not in str(num):
            count += 1
    return count

def dont_give_me_five(start, end):
    numbers = [i for i in range(start, end+1) if "5" not in str(i)]
    return len(numbers)

def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))

###14

"""You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3"""

def stray(arr):
    min_arr = min(arr)
    max_arr = max(arr)
    if arr.count(min_arr) == 1:
        return min_arr
    else:
        return max_arr

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

###15

"""Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
Note you should only return a number, the count of divisors. 
The numbers between parentheses are shown only for you to see which numbers are counted in each case."""

def divisors(n):
    a = list(range(1, 500000))
    b = 0
    for i in a:
        if n % i == 0:
            b += 1
    return b

def divisors(n):
    return sum(1 for i in xrange(1, n + 1) if n % i == 0)

###16

"""Write a function that takes an array of strings as an argument and 
returns a sorted array containing the same strings,
ordered from shortest to longest.

For example, if this array were passed as an argument:

["Telescopes", "Glasses", "Eyes", "Monocles"]

Your function would return the following array:

["Eyes", "Glasses", "Monocles", "Telescopes"]

All of the strings in the array passed to your function will be different lengths,
so you will not have to decide how to order multiple strings of the same length."""

def sort_by_length(arr):
    a = sorted(arr, key=len)
    return a

def sort_by_length(arr):
    return sorted(arr, key=len)

def sort_by_length(arr):
    arr.sort(key = len) # key sorts them by parameter of choosing
    return arr

###17

"""Your task is to split the chocolate bar of given dimension n x m into small squares. 
Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break,
but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). 
Input will always be a non-negative integer.

"""

def break_chocolate(n, m):
    return ((n * m) - 1 if n > 0 or m > 0 else 0)

def breakChocolate(n, m):
    return 0 if n*m==0 else n*m-1

def breakChocolate(n, m):
    return max(m * n - 1, 0)

###18

"""Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5"""

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b

def arithmetic(a, b, operator):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y
    }
    return operations[operator](a, b)

def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]

###19

"""As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

Another example (just to make sure it is clear):

gimme([5, 10, 14]) => 1
10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1."""

def gimme(input_array):
    arr_min = min(input_array)
    arr_max = max(input_array)
    for i, arr in enumerate(input_array):
        if arr != arr_min and arr != arr_max:
            return i

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

###20

"""The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, then don't add it to the sum. See the 4th example below.

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)"""

def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    list_1 = list(range(begin_number, end_number+1, step))
    return sum(list_1)

def sequence_sum(begin_number, end_number, step):
    return sum(list(range(begin_number, end_number + 1, step))) if begin_number <= end_number else 0

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))
