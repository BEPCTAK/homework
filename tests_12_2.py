import unittest
from runner import Runner, Tournament


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in list(self.participants):  # Используем список для итерации
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name  # Сохраняем имя бегуна
                    place += 1
                    self.participants.remove(participant)  # Удаляем финишировавшего участника
                    break  # Прерываем цикл для следующего раунда
        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем бегунов с заданными именами и скоростями
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nTournament Results:")
        for result in cls.all_results.values():
            print(result)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)

        results = tournament.start()
        TournamentTest.all_results[1] = results

        # Проверяем правильность результатов
        self.assertTrue(results[1] == "Usain")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)

        results = tournament.start()
        TournamentTest.all_results[2] = results

        # Проверяем правильность результатов
        self.assertTrue(results[1] == "Andrey")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)

        results = tournament.start()
        TournamentTest.all_results[3] = results

        # Проверяем правильность результатов
        self.assertTrue(results[1] == "Usain")