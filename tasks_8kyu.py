###1

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once."""

def solution(number):
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

###2

"""Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"""

def spin_words(sentence):
    sp_sentence = sentence.split()
    result = []
    for i in sp_sentence:
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)

###3

"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

"""

def find_it(seq):
    my_dict = {}
    for i in seq:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for key, value in my_dict.items():
        if value % 2 != 0:
            return key

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

###4

"""You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases."""

def likes(names):
    if names is None:
        return "no one likes this"
    elif len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

###5

"""Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def digital_root(n):
    sn = str(n)
    while len(sn) > 1:
        sn = str(sum(int(i) for i in sn))
    return int(sn)

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
    # ...
    while n>9:
        n=sum(map(int,str(n)))
    return n

###6

"""Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""

def array_diff(a, b):
    res = []
    for i in a:
        if i not in b:
            res.append(i)
    return res

def array_diff(a, b):
    return [x for x in a if x not in b]

###7

"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

"""

def create_phone_number(n):
    one = "".join(map(str, n[:3]))
    two = "".join(map(str, n[3:6]))
    three = "".join(map(str, n[-4:]))
    return f"({one}) {two}-{three}"

def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

###8

"""Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case"""

def count_bits(n):
    b = bin(n)
    return b.count("1")

def count_bits(n):
    return bin(n).count("1")

###9

"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
"""

def find_outlier(integers):
    odd_num = [i for i in integers if i % 2 != 0]
    even_num = [i for i in integers if i % 2 == 0]
    if len(odd_num) == 1:
        return odd_num[0]
    else:
        return even_num[0]

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

###10

"""Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""

def duplicate_count(text):
    lower_text = text.lower()
    dubl = {}
    counts = 0
    for i in lower_text:
        if i in dubl:
            dubl[i] += 1
            if dubl[i] == 2:
                counts += 1
        else:
            dubl[i] = 1
    return counts

def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

###11

"""The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!"""

def duplicate_encode(word):
    word = word.lower()
    res = ''
    for i in word:
        if word.count(i) == 1:
            res += '('
        else:
            res += ')'
    return res

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

###12

"""You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!)."""

def is_valid_walk(walk):
    we = 0
    ns = 0
    time = 0
    for i in walk:
        if i == 'n':
            ns += 1
        elif i == 's':
            ns -= 1
        elif i == 'e':
            we += 1
        elif i == 'w':
            we -= 1
        time += 1
    if ns == 0 and we == 0 and time == 10:
        return True
    else:
        return False

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

def isValidWalk(walk):
    #Reduced time with dictionary count
    my_dict = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for i in walk:
        my_dict[i] += 1
        
    if (len(walk) == 10 and 
    my_dict['n'] == my_dict['s'] and 
    my_dict['e'] == my_dict['w']):
        return True
    return False

###13

"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)"""

def persistence(n):
    if n < 10:
        return 0
    
    count = 0
    while n > 9:
        t = 1
        for i in str(n):
            t *= int(i)
        n = t
        count += 1
    return count

###14

"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"""

def to_camel_case(text):
    new = text.replace('-', ' ').replace('_', ' ')
    words = new.split()
    if not words:
        return ""
    res = [words[0]] + [i.capitalize() for i in words[1:]]
    return ''.join(res)

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

###15

"""A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.

This may be True and False in your language, e.g. PHP.

Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function."""

def narcissistic( value ):
    str_value = str(value)
    n = len(str_value)
    res = sum(int(i)**n for i in str_value)
    return res == value

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

###16

"""Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  """

def order(sentence):
    words = sentence.split()
    result = [''] * len(words)
    for word in words:
        index = int(''.join([char for char in word if char.isdigit()])) -1
        result[index] = word
    return ' '.join(result)

def order(sentence):
    return " ".join(sorted(sentence.split(), key=min))

###17

"""Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]"""

def tribonacci(signature, n):
    a1, a2, a3 = signature
    trib = [a1, a2, a3]
    for i in range(3, n):
        a1, a2, a3 = a2, a3, a1 + a2 + a3
        trib.append(a3)
    return trib[:n]

def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

###18

"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]"""

def unique_in_order(sequence):
    if not sequence:
        return []
    res = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i -1]:
            res.append(sequence[i])
    return res

###19

"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""

def solution(s):
    res = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            res.append(s[i] + s[i+1])
        else:
            res.append(s[i] + "_")
    return res

def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

###20

"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance."""

def find_uniq(arr):
    res = {}
    for i in arr:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    for index, i in res.items():
        if i == 1:
            return index

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
