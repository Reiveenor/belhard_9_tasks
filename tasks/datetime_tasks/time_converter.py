"""
Написать функцию convert_date, которая будет конвертировать время
из одной временной зоны в другую.

Функция должна принимать 3 аргумента: timestamp, current_zone, new_zone.

Функция должна возвращать время в новой временной зоне.
"""

from datetime import datetime

import pytz


def convert_date(timestamp, current_zone, new_zone):
    current_time = datetime.fromtimestamp(timestamp)
    current_tz_object = pytz.timezone(current_zone)
    new_tz_object = pytz.timezone(new_zone)
    local_timestamp = current_tz_object.localize(current_time)
    return local_timestamp.astimezone(new_tz_object)


if __name__ == '__main__':
    print(convert_date(1594823426, "US/Eastern", "US/Pacific"))
