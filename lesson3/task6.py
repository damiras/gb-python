"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def capitalize_text(text: str):
    if not text:
        return text
    diff_en = ord('z') - ord('Z')
    diff_ru = ord('я') - ord('Я')
    first_char = text[:1]
    if ord('a') <= ord(first_char) <= ord('z'):
        first_char = chr(ord(first_char) - diff_en)
    elif ord('а') <= ord(first_char) <= ord('я'):
        first_char = chr(ord(first_char) - diff_ru)
    return first_char + text[1:]


capitalized_strings = []
strings_to_capitalize = input("Введите текст: ").split(' ')
for string in strings_to_capitalize:
    capitalized_strings.append(capitalize_text(string))
result_text = ' '.join(capitalized_strings)
print(result_text)
