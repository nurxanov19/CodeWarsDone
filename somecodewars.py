import math
from math import factorial, sqrt
from functools import reduce

# 1. Har bir sonni raqamlar soniga ko'paytiring (map + lambda). Masalan: 123 -> 123 * 3 = 369
num_var = 12345

func = lambda x: len(str(x)) * x                            
#print(func(num_var))

func2 = list(map(lambda x: x * len(str(x)), [12, 234, 483, 938433, 10000000000]))
#print(func2)

def func3(obj):
    return list(map(lambda x: x * len(str(x)), [obj] if isinstance(obj, int) else obj))

#print(func3(num_var))


# 2. Ro'yxatdagi har bir so'zda nechta kichik, nechta katta harf borligini hisoblab, (kichik, katta) ko'rinishida qaytaring.
words = ['SaloM', 'dunyo', 'BuguNN', 'haVO', 'juDa', 'YAXSHI']
def zipped(lst: str):
    return tuple(zip(list(map(lambda x: sum(1 for c in x if c.islower()), lst)),\
                      list(map(lambda x: sum(1 for i in x if i.isupper()), lst))))

#print(zipped(words))


# 3. Sonlar ro'yxatidan berilgan songa eng yaqin juft sonni topib, kvadratini hisoblang (filter + map + lambda).
num_lst = [9, 7, 6, 13, 15, 29, 2, 32, 22]
def even_number(lst, given_num):
    if given_num not in lst:
        return "This number doesn't excist"
    
    return list(map(lambda s: s**2, list(filter(lambda x: x%2==0, lst[lst.index(given_num):]))))[0]

#print(even_number(num_lst, 7))

def even_number_new(lst, integer):
    even = list(filter(lambda x: x%2==0, lst))
    span = list(map(lambda i: abs(i-integer), even))
    return even[span.index(min(span))] ** 2

#print(even_number_new(num_lst, 3))

# 4. Har bir matndagi harflarni 2 martadan ortiq qatnashganlarini olib tashlab yangi so'z yarating (map + lambda).
my_str = 'gozallik dunyoni qutqaradi'
new = []
def modify(text: str):
    return list(map(lambda matn: ''.join([harf for harf in matn if matn.count(harf) < 2]), text.split()))

#print(modify(my_str))

text = 'nimadir'
new = ''
for i in text:
    if text.count(i) > 1:
        new = text.replace(i, '')

    
#print(new)


# 5. Berilgan 3 ta ro'yxatdan zip orqali uchliklar yarating, faqat ularning yig'indisi 100 dan oshganlarini qoldiring.

lst1 = [45,12,88,3,76,59,21,91,6]
lst2 = [98,17,55,32,81,67,4,73,29]
lst3 = [15,62,9,41,78,25,50,85,38]

#zipped = tuple(zip(lst1, lst2, lst3))
result = list(filter(lambda x: sum(x) < 100, tuple(zip(lst1, lst2, lst3))))
#print(result)

# 6. Har bir sonni uning raqamlarining faktoriallari yig'indisiga aylantiring (map + lambda)

result = list(map(lambda x: sum([factorial(int(i)) for i in str(x)]), lst1))
#print(result)

result2 = list(map(lambda x: sum([reduce(lambda a, b: int(a) * int(b), range(1, int(i)+1)) for i in str(x)]), lst1))
#print(result2)


# 7. Ro'yxatdagi har bir sonning kvadrat ildizini hisoblab, faqat butun chiqadiganlarni ajrating (map + filter + lambda).

seventh = list(map(int, list(filter(lambda x: str(float(x))[-1] == '0', list(map(sqrt, lst3))))))

# print()
# print(seventh)


# 8. Berilgan string-lardan faqat uzunligi tub son bo'lganlarini qoldiring (filter + lambda).

my_strs = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "plum", "quince"]
def complex(str: str):
    
    collect = []
    for j in str:
        counter = 0
        for i in range(1, len(j)+1):
            if len(j)%i == 0:
                counter += 1
        if counter == 2:
            collect.append(j)
    return collect
#print(complex(my_strs))


def complex2(str: str):
    counter = 0
    for i in range(1, len(str)+1):
        if len(str) % i == 0:
            counter += 1

    if counter == 2:
        return True
    return False
    
eightth = list(filter(lambda x: complex2(x), my_strs))
#print(eightth)

# 9. Har bir so'zdagi harflarni alfavit bo'yicha teskari qilib yozing, so'ng bosh harf bilan yozing (map + lambda).

ninth = list(map(lambda x: ''.join(sorted(x, reverse=True)).capitalize(), my_strs))
#print(ninth)


# 10.Ro'yxatdagi sonlarni faqat juft sonlargina kvadrat qilib yangi ro'yxat qaytaring (filter + map + lambda).
my_int = [12, 47, 85, 3, 19, 64, 31, 78, 6, 92, 53, 22, 49, 14, 89, 35, 7, 61, 26, 40]
tenth = list(map(lambda x: x**2, list(filter(lambda x: x % 2 == 0, my_int))))
#print(tenth)




# 11.Har bir sonni raqamlar yig'indisiga almashtiring (map + lambda bilan).Masalan: 123 -> 6, 57 -> 12
bigger_int = [7832, 167, 9455, 3201, 5123, 8844, 602, 9989, 4756, 221, 7429, 3398, 6058, 4309, 871, 2967, 1229, 6861, 9113, 5478]
eleventh = list(map(lambda x: sum([int(i) for i in str(x)]), bigger_int))
#print(eleventh)


# 12.Ro'yxatdagi faqat barcha harflari bir xil bo'lgan so'zlarni ajrating (filter + lambda bilan). Masalan: 'aaa', 'bbbb', 'abc', 'aaa', 'bbbb'
my_list = ["aaa", "bbbb", "eeeeee", "gg", "sunshine", "tranquility", "banana", "gentle", "harmony", "freedom", "inspiration", "zigzag"]
twelfth = list(filter(lambda x: set(x[0]) == set(x), my_list))
#print(twelfth)



# 13.Berilgan ro'yxatdagi faqat 3 ga karrali sonlarni ajratib oling, va ularning faktorialini hisoblang (filter + map + lambda).
lst1 = [4,12,88,3,76,59,21,91,6]
thirteenth = list(map(math.factorial  ,list(filter(lambda x: x % 3 == 0, lst1))))
#print(thirteenth)


# 14.Ro'yxatdagi har bir sonni o'z indeksiga ko'paytiring (map + enumerate + lambda).Masalan: [4, 5, 6] > [0*4, 1*5, 2*6] > [0, 5, 12]
fortinth = list(map(lambda x: x[0] * x[1], enumerate(lst1)))
#print(fortinth)


# 15.Ro'yxatdagi faqat palindrom bo'lgan so'zlarni ajrating va ularni bosh harf qilib yozing (filter + map + lambda).
mixed_list = ["madam", "apple", "racecar", "banana", "level", "orange", "radar", "grape", "civic", "mango", "refer", "pear"]

fiftinth = list(map(lambda x: x.capitalize() , list(filter(lambda x: x[::-1] == x, mixed_list))))
#print(fiftinth)


"""
8-oy / 1-dars uchun berilgan uy ishi
"""

# 1. Berilgan sonlar ro'yxatidan faqat tub sonlarni ajratib oling (filter + lambda yordamida). Tub sonni aniqlovchi funksiyani lambda orqali yozing.
prime_number = list(filter(lambda x:  all([x % i for i in range(2, x)]), lst1))
#print(prime_number)


# 2. Berilgan sonlar ro'yxatidagi har bir sonning faktorialini hisoblang (map + lambda bilan).
def some_func():
    factorial_ = []
    for i in list(map(lambda x: [i for i in range(1, x+1)], [7, 24, 18, 9])):
        factorial_.append(reduce(lambda a, b: a * b, i))
    return factorial_

#print(some_func())
#print(list(map(lambda x: reduce(lambda a, b: a * b, [i for i in range(1, x+1)]), [7, 24, 18, 9])))  # 2-yo'li



# 3. Har bir so'zdan unli harflar sonini hisoblab ro'yxat qaytaring (map + lambda bilan). So'zlar ro'yxati matn ko'rinishida beriladi.
vowels = ['a', 'e', 'i', 'o', 'u']
my_string = "This is a string that spans multiple lines"
vowels_func = list(map(lambda x:  len([i for i in x if i in vowels]), my_string.split()))
#print(vowels_func)


# 4. Sonlar ro'yxatidan faqat palindrom (teskari yozilganda o'zgarmaydigan) sonlarni ajratib oling (filter + lambda).
mixed_list = ["madam", "apple", "racecar", "banana", "level", "orange", "radar", "grape", "civic", "mango", "refer", "pear"]
polindrome = list(filter(lambda x: x == x[::-1], mixed_list))
#print(polindrome)



# 5. Matnlar ro'yxatidan faqat anagrammalar juftligini ajrating. (map + filter + lambda bilan).
words_list = [
    "silent",  "listen", "married", "admirer", "stressed", "desserts", "dusty", "study", "save", "vase", "apple",  
    "banana", "cherry", "grape", "orange"    
]

anagram = list(filter(lambda x: list(map(sorted, words_list)).count(sorted(x)) > 1, words_list))
print(anagram)

# 6. Berilgan so'zlar ro'yxatida eng uzun so'zni reduce orqali toping.
longer = reduce(lambda a, b: a if len(a) >= len(b) else b , my_string.split())
print(longer)


# 7. Berilgan sonlar ro'yxatidagi eng katta farqni (maks va min orasidagi farq) reduce orqali hisoblang.
difference = len(reduce(lambda a, b: a if len(a) >= len(b) else b , my_string.split())) - len(reduce(lambda a, b: a if len(a) <= len(b) else b , my_string.split()))
print(difference)

# 8. Har bir so'zdagi unli harflarni olib tashlab, faqat undosh harflardan iborat yangi so'zlar ro'yxatini yarating (map + lambda).
vowels = ['a', 'e', 'i', 'o', 'u']
extract_vowels = list(map(lambda x: ''.join([i for i in x if i not in vowels]), words_list))
print(extract_vowels)


# 9. Ro'yxatda faqat bir marta qatnashgan elementlarni ajratib oling (filter + lambda yordamida).
example_list = [2, 2, 3, 3, 3, 4, 4, 4, 4, 1]  # Unique element is 1

appear_one = list(filter(lambda x: example_list.count(x) == 1, example_list))
print(appear_one)

# 10. 2 ta matnlar ro'yxatidan har bir elementini birlashtirib yangi ro'yxat yarating, va faqat uzunligi 10 dan oshganlarini tanlab oling (map + filter + lambda bilan).
fruits = ["apple", "banana", "cherry", "grape", "orange"]
colors = ["red", "blue", "green", "yellow", "purple"]

attach = list(filter(lambda x: len(x)> 10, list(map(lambda x: x[0] + x[1], list(zip(fruits, colors))))))
print(attach)

