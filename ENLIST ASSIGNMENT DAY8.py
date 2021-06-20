dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dict2 = {5: 'e', 6: 'f', 7: 'g'}
print(dict2)
dict3 = {**dict1, **dict2}  # method 1
dict2.update(dict1)  # method 2
print(dict1)
print(dict3)
print(dict2)

list1 = [2, 3, 4, 5, 6, 7, 1, 2, 3, 43, 12, 14]
list1.sort()  # sort list in ascending order
print(list1)
list1.sort(reverse=True)
print(list1)

set1 = set(list1)
print(set1)
type(set1)
type(list1)

dict1 = {'Ram': [12, 13, 21, 16], 'Kevin': [12, 67, 54, 43], 'John': [34, 87, 88, 98], 'Sam': [33, 66, 55, 44]}
result = {k: sorted(dict1[k]) for k in sorted(dict1)}
print(result)


def function1(dict1):
    res = dict()
    for key in sorted(dict1):
        res[key] = sorted(dict1[key])
    return res


function1(dict1)


def function2(dict1):
    res = dict()
    min1 = dict1[key]
    for key in sorted(dict1):
        if dict1[key] < min1:
            min1 = dict1[key]
            res[key] = min1
    return res


function1(dict1)


def fun():
    user = input("Enter the string :")
    word = "String is given by user  "
    return user + word[6:]


fun()


def fun1():
    user = input("Enter the string :")
    word = "String is given by user  "
    return word.replace('String', user)


fun1()


def fun3():
    user = input("Enter the string :")
    return user.capitalize()


fun3()


def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, str1[0].upper())
    str1 = char + str1[1:]
    return str1


change_char('hello world !')
from collections import Counter

l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item] > 1])
print(new_list)


def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(list1))

a = int(input("Enter number :"))
b = int(input("Enter number :"))
c = int(input("Enter number :"))
sum1 = a + b + c
print(sum1)
user = int(input("Enter the number to divide sum!"))
if sum1 % user == 0:
    print("The given input divide")
else:
    print("The given input does not divide sum1")

from collections import Counter


def MMM(n_num):
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n // 2]
        median2 = n_num[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = n_num[n // 2]
    print("Median is: " + str(median))
    data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    print(get_mode)


l = [12, 11, 23, 245, 25, 22, 344, 34, 56]
MMM(l)

a = "Hello"
b = "World"
tep = a
a = b
b = tep
print(a, b)
x = a
y = b
x, y = y, x
print(x, y)


def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")


n = 65
decToOctal(n)
n = 3
decToOctal(n)
