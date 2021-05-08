"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from json import dump

profits = []
companies_profits = {}

input_filename = 'task7.dat'
output_filename = 'task7.dat.json'

with open(input_filename, 'r', encoding='utf-8') as df, open(output_filename, 'w', encoding='utf-8') as jf:
    for row in df:
        row_data = row.split()
        company_name = row_data[0]
        company_profit = float(row_data[2]) - float(row_data[3])
        companies_profits[company_name] = company_profit
        if company_profit > 0:
            profits.append(company_profit)
    average_profit = sum(profits) / len(profits)
    result = [companies_profits, {'average_profit': average_profit}]
    dump(result, jf, ensure_ascii=False, indent=4)
