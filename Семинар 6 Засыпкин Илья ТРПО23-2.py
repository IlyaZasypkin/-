#Задача 1

# Перечисление
numbers_list1 = [31, 24, 17]
print(numbers_list1)  # [31, 24, 17]

# На основе другого списка (копирование)
numbers_list2 = numbers_list1.copy()
print(numbers_list2)  # [31, 24, 17]

# С помощью функции range
numbers_list3 = list(range(31, 16, -7))
print(numbers_list3)  # [31, 24, 17]

# Создание и вывод списка из полученных списков
combined_list = [numbers_list1, numbers_list2, numbers_list3]
print(combined_list)  # [[31, 24, 17], [31, 24, 17], [31, 24, 17]]

#Задача 2.1

user_string = input("Введите строку: ")
characters_list = list(user_string)
print(characters_list)

#Задача 2.2

words_list = user_string.split()
print(words_list)

#Задача 2.3

digits_list = [char for char in user_string if char.isdigit()]
print(digits_list)

#Задача 3

# Исходный список
original_list = ['input', 'string', 'repeat', 3]

# Проверка на вхождение слова "repeat" и наличие последнего элемента как числа
if 'repeat' in original_list and isinstance(original_list[-1], int):
    # Создаем новый список с копиями всех элементов, кроме последних двух
    new_list = original_list[:-2] * original_list[-1] + original_list[-2:]
    print(new_list)
else:
    print("Список не удовлетворяет условию")
    
#Задача 4

# Произвольные строки
s1 = "apple"
s2 = "banana"

# Создание списка из строк, их длин и результата проверки лексикографического порядка
result_list = [s1, s2, len(s1), len(s2), s1 < s2]

# Проверка параметра output
output = 'order'
if output == 'lengths':
    print(f"Длины строк: {result_list[2]} и {result_list[3]}")
elif output == 'order':
    if result_list[4]:
        print(f"Строка '{result_list[0]}' идет ПЕРЕД строкой '{result_list[1]}'")
    else:
        print(f"Строка '{result_list[0]}' идет ПОСЛЕ строки '{result_list[1]}'")
else:
    print("Некорректное значение параметра output")
    
#Задача 5.1
    
# Запрос у пользователя двух целых чисел
max_val = int(input("Введите первое целое число: "))
repeat = int(input("Введите второе целое число: "))

# Создание списка из целых чисел
result_list = [i for i in range(1, max_val + 1) for _ in range(repeat)]

# Вывод результата
print(result_list)

#Задача 5.2

# Создание копии списка
copied_list = result_list[:]

# Определение количества элементов для удаления
num_to_remove = int(len(copied_list) * 0.8)

# Удаление 80% элементов из середины
del copied_list[len(copied_list)//2 - num_to_remove//2 : len(copied_list)//2 + num_to_remove//2]

# Умножение элементов исходного списка, которые не сохранены в скопированном списке, на 10
for i in range(len(result_list)):
    if result_list[i] not in copied_list:
        result_list[i] *= 10

# Вывод результатов
print("Исходный список:", result_list)
print("Копия списка с удаленными элементами:", copied_list)
