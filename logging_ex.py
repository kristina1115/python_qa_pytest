import logging

# создаем logger (объект, который говорит, что логировать)
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG) # уровень логирования

# создаем formatter (говорит в каком формате записывать логи)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# создаем консольный handler и задаем уровень (что записывать и где слушать)
handler = logging.FileHandler('log_ex.log')
handler.setLevel(logging.DEBUG)

# добавляем formatter в ch
handler.setFormatter(formatter)

# добавляем ch в logger
logger.addHandler(handler)

# код приложения
logger.debug('debug message')
#logger.info('info message')
#logger.error('error message')
#logger.critical('critical message')
#logger.warning('warning message')


def test_division(x,y):
    try:
        x/y
        logger.info(f"x/y successful with result: {x/y}.")
    except ZeroDivisionError:
        logger.exception("ZeroDivisionError")

test_division(2,0)

