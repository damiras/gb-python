"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

from datetime import datetime


def is_valid_birth_year(year: str) -> bool:
    """
    Проверяет является ли строка валидным годом рождения.
    :param str year:
    :return: bool
    """
    if not year:
        return True
    try:
        year = int(year)
        max_age = 150
        current_year = datetime.now().year
        if year > current_year or year < current_year - max_age:
            return False
        return True
    except ValueError:
        return False


def print_user_info(name: str = '', surname: str = '', birth_year: str = '',
                    city: str = '', email: str = '', phone: str = ''):
    output_info = name.title() if name else ''
    output_info += ' ' + surname.title() if surname else ''
    output_info += ' ' + birth_year + ' года рождения' if birth_year else ''
    output_info += ' из города ' + city if city else ''
    if email or phone:
        output_info += ' ('
        output_info += 'email: ' + email if email else ''
        output_info += (', ' if email else '') + 'телефон: ' + phone if phone else ''
        output_info += ')'
    print(output_info)


input_data = {
    'name': 'имя',
    'surname': 'фамилию',
    'birth_year': 'год рождения',
    'city': 'город проживания',
    'email': 'E-mail',
    'phone': 'телефон'
}

for k, label in input_data.items():
    input_data[k] = input(f"Введите {label} пользователя: ").strip()
    if k == 'birth_year' and input_data[k]:
        while not is_valid_birth_year(input_data[k]):
            print('Вы ввели неверный год рождения!')
            input_data[k] = input(f"Введите {label} пользователя: ").strip()

print_user_info(name=input_data['name'], surname=input_data['surname'], birth_year=input_data['birth_year'],
                city=input_data['city'], phone=input_data['phone'], email=input_data['email'])
