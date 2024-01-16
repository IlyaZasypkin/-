#Задача 1
import re

input_string = 'aaa--bbb==ccc__ddd'
result = re.split('--|==|__', input_string)
print(result)  # ['aaa', 'bbb', 'ccc', 'ddd']

#Задача 2
input_string = 'Yesterday, All my troubles seemed so far away'
first_word = input_string.split()[0]
print(first_word)  # 'Yesterday'

#Задача 3
input_string = 'Yesterday, All my troubles seemed so far away'
last_word = input_string.split()[-1]
print(last_word)  # 'away'

#Задача 4
import re

input_string = "In the beginning God created the heavens and the earth."
vowel_words = re.findall(r'\b[aeiouAEIOU][a-zA-Z]*\b', input_string)
print(vowel_words)  # ['In', 'and']

#Задача 5
input_string = """In the beginning
When I was young
I'd listen to the radio"""
first_words = [line.split()[0] for line in input_string.split('\n') if line]
print(first_words)  # ['In', 'When', "I'd"]

#Задача 6
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

email = "example@example.com"
print(validate_email(email))  # True

#Задача 7
import re

input_string = "Email me at example1@example.com or info@example.org"
domains = re.findall(r'@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', input_string)
print(domains)  # ['example.com', 'example.org']

#Задача 8
import re

def validate_phone_number(phone_number):
    pattern = r'^\+7\s?\(?\d{3}\)?\s?\d{3}-?\s?\d{2}-?\s?\d{2}$'
    return bool(re.match(pattern, phone_number))

phone_number = "+7 (999) 999-99-99"
print(validate_phone_number(phone_number))  # True

