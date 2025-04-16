import math
# 1. Har bir sonni raqamlar soniga ko'paytiring (map + lambda). Masalan: 123 -> 123 * 3 = 369
num_var = 12345

func = lambda x: len(str(x)) * x                            
print(func(num_var))

func2 = list(map(lambda x: x * len(str(x)), [12, 234, 483, 938433, 10000000000]))
print(func2)

def func3(obj):
    return list(map(lambda x: x * len(str(x)), [obj] if isinstance(obj, int) else obj))

print(func3(num_var))


# 2. Ro'yxatdagi har bir so'zda nechta kichik, nechta katta harf borligini hisoblab, (kichik, katta) ko'rinishida qaytaring.
words = ['SaloM', 'dunyo', 'BuguNN', 'haVO', 'juDa', 'YAXSHI']
def zipped(lst: str):
    return tuple(zip(list(map(lambda x: sum(1 for c in x if c.islower()), lst)),\
                      list(map(lambda x: sum(1 for i in x if i.isupper()), lst))))

print(zipped(words))


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

print(even_number_new(num_lst, 3))

# 4. Har bir matndagi harflarni 2 martadan ortiq qatnashganlarini olib tashlab yangi so'z yarating (map + lambda).
my_str = 'gozallik dunyoni qutqaradi'
new = []
def modify(text: str):
    return list(map(lambda matn: ''.join([harf for harf in matn if matn.count(harf) < 2]), text.split()))

print(modify(my_str))

text = 'nimadir'
new = ''
for i in text:
    if text.count(i) > 1:
        new = text.replace(i, '')

    
print(new)


# 5. Berilgan 3 ta ro'yxatdan zip orqali uchliklar yarating, faqat ularning yig'indisi 100 dan oshganlarini qoldiring.

lst1 = [45,12,88,3,76,59,21,91,6]
lst2 = [98,17,55,32,81,67,4,73,29]
lst3 = [15,62,9,41,78,25,50,85,38]

zipped = tuple(zip(lst1, lst2, lst3))
result = list(filter(lambda x: sum(x) < 100, tuple(zip(lst1, lst2, lst3))))
print(result)