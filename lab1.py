from copy import copy


class WorkWithStr:
    """Работа со строкой"""

    def __init__(self, string):
        self.string = string
        self.len_str()
        self.reverse_str()
        self.copy_str()
        self.summ_str()

    def len_str(self):
        """Длина строки"""
        return print(f'Длина строки: {len(self.string)}')

    def reverse_str(self):
        """Инверсия строки"""
        return print(f'Инверсия строки: {self.string[::-1]}')

    def copy_str(self):
        """Копирование строки"""
        return print(f'Начальная строка: {self.string} \nСкопированное значение {copy(self.string)}')

    def summ_str(self):
        return print(f'Обьединение строк: {self.string + self.string}')


if __name__ == '__main__':
    init = WorkWithStr(str(input("Введите текст: ")))
