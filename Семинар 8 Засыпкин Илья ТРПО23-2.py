#Задача 1

l1 = ['1', '123', '123', '12', '1', '123']
length_list = [len(item) for item in l1]
print(length_list)

#Задача 2

l1 = ['1', '123', '123', '12', '1', '123']
count = sum(1 for x in l1 if len(x) > 2)
print(count)

#Задача 3

l2 = [2, 4, -2, -3, 0, 11, 3, -1]
result = [x * i for i, x in enumerate(l2)]
print(result)

#Задача 4

l2 = [2, 4, -2, -3, 0, 11, 3, -1]
result = [x for x in l2 if x >= 0]
print(result)

#Задача 5

l2 = [2, 4, -2, -3, 0, 11, 3, -1]
result = [i if x < 0 else x for i, x in enumerate(l2)]
print(result)

#Задача 6

s = 'abcdef'
result = {char: i+1 for i, char in enumerate(s)}
print(result)

#Задача 7

l1 = ['1', '123', '123', '12', '1', '123']
d1 = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50}
count = sum(1 for x in l1 if x in d1)
print(count)

#Задача 8

evgene_o = "example_string"
result = {char: evgene_o.count(char) for char in set(evgene_o)}
print(result)

#Задача 9

evgene_o = "example_string"
result = sum(1 for char in evgene_o if char.islower())
print(result)

#Задача 10

d4 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
result = sum(k*v for k, v in d4.items())
print(result)

#Задача 11

d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
d7 = {k: v for k, v in d6.items() if k not in d5}
print(d7)

#Задача 12

d5 = {'a': 3, 'b': 4, 'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9}
d6 = {'e': 20, 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 26, 'l': 27}
d8 = {k: d6[k] if k in d6 else v for k, v in d5.items()}
print(d8)



