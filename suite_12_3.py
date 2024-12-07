import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание тестового набора
if __name__ == '__main__':
    suite = unittest.TestSuite()

    # Добавление тестов в TestSuite
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)