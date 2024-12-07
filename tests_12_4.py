import logging
import unittest
from runner import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)



class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Вося", -5)  # Передаем отрицательное значение скорости
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем некорректный тип для имени
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)


if __name__ == '__main__':
    unittest.main()
