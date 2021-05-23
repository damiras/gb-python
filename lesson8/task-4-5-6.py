"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка:
постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class DeptNotFoundError(Exception):
    pass


class EquipmentShipUnavailableError(Exception):
    pass


class OfficeEquipment(ABC):
    @abstractmethod
    def __init__(self, model: str = None, color: str = None, price: float = None):
        pass

    @property
    @abstractmethod
    def equipment_type(self) -> str:
        pass

    def __str__(self):
        name = self.equipment_type()
        if self.model:
            name += ' ' + self.model
        if self.color:
            name += ' ' + self.color
        return name


class Warehouse:
    _shipped = {}
    _storing = {}

    # зарегистрировать отдел
    def book_dept(self, dept_name: str):
        if type(dept_name) != str:
            raise TypeError("Dept name must be a string value!")
        dept_name = dept_name.strip()
        if not dept_name:
            raise ValueError("Dept name cannot be empty!")
        if dept_name not in self._shipped:
            self._shipped[dept_name] = []

    # добавить товар на склад
    def store(self, equipment: OfficeEquipment, count: int = 1):
        if not isinstance(equipment, OfficeEquipment):
            raise TypeError("Invalid equipment type!")
        try:
            count = int(count)
        except ValueError:
            raise TypeError("Equipment count must be an integer value!")
        if count >= 1:
            if equipment.equipment_type not in self._storing:
                self._storing[equipment.equipment_type] = []
            self._storing[equipment.equipment_type].append({'ware': equipment, 'date': datetime.now(), 'count': count})

    # посчитать количество товара (со свойствами) на складе
    def count_storing_equipment(self, equipment: OfficeEquipment) -> int:
        if not isinstance(equipment, OfficeEquipment):
            raise TypeError("Invalid equipment type!")
        eq_type = equipment.equipment_type
        if eq_type not in self._storing:
            return 0
        count = 0
        for record in self._storing[equipment.equipment_type]:
            if type(record['ware']) == type(equipment):
                if equipment.model is not None and record['ware'].model != equipment.model:
                    continue
                if equipment.color is not None and record['ware'].color != equipment.color:
                    continue
                count += record['count']
        return count

    # отгрузить товар со склада в отдел
    def ship(self, equipment: OfficeEquipment, to_department: str, count: int = 1):
        if not isinstance(equipment, OfficeEquipment):
            raise TypeError("Invalid equipment type!")
        if type(to_department) != str:
            raise TypeError("Department must be a string value!")
        if to_department not in self._shipped:
            raise DeptNotFoundError(f'Department "{to_department}" not found!')
        try:
            count = int(count)
        except ValueError:
            raise TypeError("Equipment count must be an integer value!")
        if count >= 1:
            if self.count_storing_equipment(equipment) < count:
                raise EquipmentShipUnavailableError(f"Cannot ship {count} equipment of type {equipment.equipment_type}")
            # мы не удаляем товар, а добавляем запись об отгрузке товара (-count), чтобы информация сохранялась
            self._storing[equipment.equipment_type].append({'ware': equipment, 'date': datetime.now(), 'count': -count})
            # отружаем в нужный отдел
            self._shipped[to_department].append({'ware': equipment, 'date': datetime.now(), 'count': count})


class Organization:
    def __init__(self, warehouse: Warehouse, departments: list):
        if not isinstance(warehouse, Warehouse):
            raise TypeError("Invalid warehouse type!")
        self._warehouse = warehouse
        if not isinstance(departments, (tuple, list)):
            raise TypeError("Departments must be list of strings!")
        if not departments:
            raise ValueError("List of departments cannot be empty!")
        self._departments = departments
        for dept in departments:
            self._warehouse.book_dept(dept)

    @property
    def warehouse(self) -> Warehouse:
        return self._warehouse

    def add_dept(self, dept_name: str):
        self._warehouse.book_dept(dept_name)


class Printer(OfficeEquipment):
    def __init__(self, model: str = None, color: str = None, price: float = None, is_color: bool = False):
        self.model = model
        self.color = color
        self.price = price
        self.is_color = is_color

    def equipment_type(self) -> str:
        return 'printer'


class Scanner(OfficeEquipment):
    _scanner_types = ('3D', 'планшетный', 'протяжный', 'ручной', 'слайд-сканер', 'фотоаппаратный')

    def __init__(self, model: str = None, color: str = None, price: float = None, scanner_type: str = None):
        self.model = model
        self.color = color
        self.price = price
        if scanner_type is None or scanner_type in self._scanner_types:
            self.scanner_type = scanner_type
        else:
            raise ValueError("Invalid scanner type!")

    def equipment_type(self) -> str:
        return 'scanner'


class Xerox(OfficeEquipment):
    def __init__(self, model: str = None, color: str = None, price: float = None):
        self.model = model
        self.color = color
        self.price = price

    def equipment_type(self) -> str:
        return 'xerox'


if __name__ == '__main__':
    org = Organization(Warehouse(), ['Отдел продаж', 'Бухгалтерия', 'Web-отдел'])
    cannon_printer = Printer('Cannon', 'white', 20000.00, True)
    hp_printer = Printer('HP', 'black', 15000, True)
    hp_scanner = Scanner('HP', 'gray', 10000, 'протяжный')
    xerox = Xerox()
    org.warehouse.store(xerox, 3)
    org.warehouse.store(hp_scanner, 5)
    org.warehouse.store(hp_printer, 4)
    org.warehouse.store(cannon_printer, 3)
    print("Всего ксероксов:", org.warehouse.count_storing_equipment(xerox))
    print("Всего сканеров HP:", org.warehouse.count_storing_equipment(hp_scanner))
    print("Всего принтеров HP:", org.warehouse.count_storing_equipment(hp_printer))
    print("Всего принтеров Cannon:", org.warehouse.count_storing_equipment(cannon_printer))
    org.warehouse.ship(cannon_printer, 'Отдел продаж', 2)
    print("Всего принтеров Cannon:", org.warehouse.count_storing_equipment(cannon_printer))
