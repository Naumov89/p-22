###1

"""Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []"""

def solution(nums):
    if nums != None:
        sorted_list = sorted(nums)
        return sorted_list
    else:
        return []

def solution(nums):
    return [] if nums == None else sorted(nums)

def solution(nums):
    return sorted(nums) if nums else []

def solution(nums):
    try:
        return sorted(nums)
    except TypeError:
        return []

###2

"""Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"""

def remove_url_anchor(url):
    for u in url:
        if "#" in url:
            index_url = url.find('#')
            new_url = url[:index_url]
            return new_url
        else:
            return url

def remove_url_anchor(url):
    return url.split('#')[0]

def remove_url_anchor(url):
    index = url.find('#')
    return url[:index] if index >= 0 else url

def remove_url_anchor(url):
    return url[:url.index('#')] if '#' in url else url

###3

"""Instructions
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]"""

def capitals(word):
    return [index for index, w in enumerate(word) if w == w.upper()]

def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]

###4

"""You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers."""

def small_enough(array, limit):
    max_array = max(array)
    if limit >= max_array:
        return True
    else:
        return False

def small_enough(array, limit):
    return max(array)<=limit

def small_enough(array, limit):
    return all(a <= limit for a in array)

###5

"""The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example (Input --> Output):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]"""

def two_oldest_ages(ages):
    sort_ages = sorted(ages)
    return sort_ages[-2:]

def two_oldest_ages(ages):
    return sorted(ages)[-2:]

###6

"""Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input --> Output)

10 --> 1
99 --> 18
-32 --> 5"""

def sum_digits(number):
    if number < 0:
        number *= -1
        return sum(int(num) for num in str(number)) 
    else:
        return sum(int(num) for num in str(number))

def sumDigits(number):
    return sum([int(i) for i in str(abs(number))])

def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))

###7

"""Notes
The parameters (divisor, bound) passed to the function are only positive values .
It's guaranteed that a divisor is Found .
Input >> Output Examples
divisor = 2, bound = 7 ==> return (6)
Explanation:
(6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .

divisor = 10, bound = 50 ==> return (50)
Explanation:
(50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*

divisor = 37, bound = 200 ==> return (185)
Explanation:
(185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .

"""

def max_multiple(divisor, bound):
    while True:
        if bound % divisor == 0:
            return bound
        else:
            bound -= 1

def max_multiple(divisor, bound):
    return bound - (bound % divisor)

def max_multiple(divisor, bound):
    return bound // divisor * divisor

###8

"""In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!"""

def solve(s):
    k = 0
    for i in s:
        if i.islower():
            k += 1
    if k >= len(s) / 2:
        return s.lower()
    else:
        return s.upper()

def solve(s):
    lower_case = [l for l in s if l.islower()]
    upper_case = [l for l in s if l.isupper()]
    
    if len(upper_case) > len(lower_case):
        return s.upper()
    return s.lower()

###9

"""In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) 
or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C)."""

def factorial(n):
    fact = list(range(n, 1, -1))
    if n == 0:
        return 1
    s = n
    for u in fact[1:]:
        s *= u
    return s

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Вхідне значення повинно бути від 0 до 12")
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n*factorial(n-1)

###10

"""ask
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates).

Notes:
Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
Input >> Output Examples
minValue ({1, 3, 1})  ==> return (13)
Explanation:
(13) is the minimum number could be formed from {1, 3, 1} , Without duplications

minValue({5, 7, 5, 9, 7})  ==> return (579)
Explanation:
(579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications"""

def min_value(digits):
    set_digits = set(digits)
    sor = sorted(set_digits)
    return int("".join(str(s) for s in sor))

def min_value(digits):
    return int("".join(map(str,sorted(set(digits)))))

def min_value(digits):
    return int("".join(str(x) for x in sorted(set(digits))))

###11

"""Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!"""

def capitalize(s):
    new_s = []
    new_s2 = []
    for index, i in enumerate(s):
        if index % 2 == 0:
            new_s.append(i.upper())
        else:
            new_s.append(i.lower())
    for index, i in enumerate(s):
        if index % 2 != 0:
            new_s2.append(i.upper())
        else:
            new_s2.append(i.lower())
    return [''.join(new_s), ''.join(new_s2)]

def capitalize(s):
    result = ['','']
    for i,c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result

def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]

###12

"""Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9]."""

def flatten_and_sort(array):
    one_array = []
    for i in array:
        for u in i:
            one_array.append(u)
    return sorted(one_array)

def flatten_and_sort(array):
    return sorted([a for ar in array for a in ar])

def flatten_and_sort(array):
    item = []
    for y in array:
        for x in y:
            item.append(x)
    
    item.sort()
    return item

def flatten_and_sort(array):
    return sorted(sum(array, []))

###13

"""Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.

For Example:

[ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
, [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
, [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
]
So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.

Note: You will always be given a non-empty list containing positive values.

ENJOY CODING :)"""

def sum_of_minimums(numbers):
    min_num = [min(num) for num in numbers] 
    return sum(min_num)

def sum_of_minimums(numbers):
    return sum(map(min, numbers))

def sum_of_minimums(numbers):
    return sum([min(num) for num in numbers])

def sum_of_minimums(numbers):
    total = 0
    for nums in numbers:
        total += min(nums)
    return total

###14

"""Are the numbers in order?
In this Kata, your function receives an array of integers as input. Your task is to determine whether the numbers are in ascending order. An array is said to be in ascending order if there are no two adjacent integers where the left integer exceeds the right integer in value.

For the purposes of this Kata, you may assume that all inputs are valid, i.e. arrays containing only integers.

Note that an array of 0 or 1 integer(s) is automatically considered to be sorted in ascending order since all (zero) adjacent pairs of integers satisfy the condition that the left integer does not exceed the right integer in value.

For example:

in_asc_order([1,2,4,7,19]) # returns True
in_asc_order([1,2,3,4,5]) # returns True
in_asc_order([1,6,10,18,2,4,20]) # returns False
in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order
N.B. If your solution passes all fixed tests but fails at the random tests, make sure you aren't mutating the input array."""

def in_asc_order(arr):
    sor_arr = sorted(arr)
    if sor_arr == arr:
        return True
    else:
        return False

def in_asc_order(arr):
    return sorted(arr) == arr

###15

"""Scenario
Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.

Notes
Array size is at least 1.
All numbers will be positive.
Input >> Output Examples
rowWeights([13, 27, 49])  ==>  return (62, 27)
Explanation:
The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
Explanation:
The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.

rowWeights([80])  ==>  return (80, 0)
Explanation:
The first element 80 is the total weight of team 1, and the second element 0 is the total weight of team 2."""

def row_weights(array):
    one_arr = []
    two_arr = []
    for index, arr in enumerate(array):
        if index % 2 != 0:
            one_arr.append(arr)
        else:
            two_arr.append(arr)
    return sum(two_arr), sum(one_arr)

def row_weights(array):
    return sum(array[::2]), sum(array[1::2])

def row_weights(array):
    a = array[::2]
    b = array[1::2]
    return sum(a),sum(b)

def row_weights(array):
    t1 = 0
    t2 = 0
    for i, n in enumerate(array):
        if i%2==0:
            t1+=n
        else:
            t2+=n
    return t1, t2

###16

"""Your task is to write function factorial."""

def factorial(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i 
    return res

def factorial(n):
    if n<2: return 1
    else: return n*factorial(n-1)

def factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

###17

"""Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'"""

def remove_duplicate_words(s):
    s_s = s.split()
    new_s = []
    for i in s_s:
        if i not in new_s:
            new_s.append(i)
    return " ".join(new_s)

def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key = s.index))

def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))

###18

"""In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000."""

def is_leap_year(year):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False  

def is_leap_year(year):
    return year % 4 ==0 and year % 100!=0 or year % 400==0

###19

"""Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer."""

def largest_pair_sum(numbers): 
    sor_numbers = sorted(numbers, reverse=True) 
    return sor_numbers[0] + sor_numbers[1]

def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])

###20

"""Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given."""

def no_odds(values):
    return [val for val in values if val % 2 == 0] 