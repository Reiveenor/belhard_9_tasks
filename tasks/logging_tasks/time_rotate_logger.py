"""
Настроить логгирование с модулем logging.

Настроить формат вывода.
Настроить, чтобы вывод шел в файл и в консоль.
Настроить ротацию файла лога по времени (полночь).
"""
import logging
from logging.handlers import TimedRotatingFileHandler

log_file = logging.getLogger(__name__)
log_file.setLevel(logging.INFO)
file = TimedRotatingFileHandler("sample.log", when='midnight')
file_format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
file.setFormatter(file_format)
log_file.addHandler(file)

stream = logging.StreamHandler()
stream_format = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s", datefmt="%H:%M:%S")
stream.setFormatter(stream_format)
log_file.addHandler(stream)


if __name__ == '__main__':
    log_file.info('some info message')
    log_file.error('some error msg')
