import unittest

def skip_if_frozen(func):
    """Декоратор для пропуска тестов, если is_frozen = True."""
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Установлено в False, тесты будут выполняться

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertIn(3, [1, 2, 3])

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Установлено в True, тесты будут пропущены

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual("A", "A")

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual("B", "B")

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertEqual("C", "C")
