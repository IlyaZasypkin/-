#Задача 1
def common_characters(str1, str2):
    common_chars = ""
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars += char
    return common_chars

string1 = "hello"
string2 = "world"
result = common_characters(string1, string2)
print(f"Общие символы: {result}")

#Задача 2
def double_factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result

number = 7
result = double_factorial(number)
print(f"Двойной факториал числа {number} равен {result}")

#Задача 3
def double_factorial(n):
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result

number = 7
result = double_factorial(number)
print(f"Двойной факториал числа {number} равен {result}")

#Задача 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

a = 10
b = 30

print(f"Простые числа в интервале от {a} до {b}:")
for num in range(a, b+1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)

#Задача 5
while True:
    user_input = input("Введите значение (или STOP для завершения): ")
    
    if user_input == "STOP":
        print("Program interrupted by user")
        break
    
    if user_input.strip() == "":
        print("Пустая строка. Попробуйте снова.")
        continue
    
    if user_input < "a":
        print("Too early in the dictionary. Try again!")
        continue
    
    formatted_string = user_input.center(30, '_')
    print(f"Отформатированная строка: {formatted_string}")
    
#Задача 6
input_string = "Hello world!"
output_string = ""

for i in range(1, len(input_string) + 1):
    if len(input_string) % i == 0:
        output_string += input_string[i-1]

print(output_string)

#Задача 7
input_string = "Hello world!"
search_string = "HERD"
output_string = ""

search_string_lower = search_string.lower()

for i, char in enumerate(input_string):
    if char.lower() in search_string_lower:
        output_string += f"{i+1} символ встречается в строке поиска: {search_string_lower.replace(char.lower(), char, 1)}\n"

print(output_string)
        
