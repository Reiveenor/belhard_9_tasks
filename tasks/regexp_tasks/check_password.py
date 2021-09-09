"""
Написать функцию check_password, которая будет принимать строку и проверять,
что она является паролем, который соответствует следующим правилам:
1. Длина от 8 до 40 символов
2. Должен включать букву верхнего регистра
3. Должен включать букву нижнего регистра
4. Должен включать цифру
5. Должен включать символ (из некоторого набора или исключения)

Подсказка:
Понадобится позитивный просмотр вперед (?=чтото)
"""
import re


def check_password(password: str):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,40}$"
    if re.fullmatch(pattern, password):
        print('Valid password')
    else:
        print('Invalid password')


if __name__ == '__main__':
    check_password('Hhyggo534@t')
    check_password('sdfgqwesdfg')
    check_password('123123123')
    check_password('</></>')
    check_password('#$%&#$')
    check_password('ghdfghasdkjfnnasdlfadsfasdflnmlkmwerlktmwre')
