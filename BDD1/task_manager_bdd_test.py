import unittest
from datetime import datetime, timedelta
from task_manager import TaskManager, Task, TaskStatus


class TaskManagerBDDTests(unittest.TestCase):
    """
    Testy BDD dla systemu zarządzania zadaniami.

    Scenariusze testowe są opisane w formacie:
    Given (Mając) - kontekst początkowy
    When (Kiedy) - akcja
    Then (Wtedy) - oczekiwany rezultat
    """

    def setUp(self):
        """Przygotowanie kontekstu testowego."""
        self.task_manager = TaskManager()

    def test_adding_new_task(self):
        """
        Scenariusz: Dodawanie nowego zadania

        Given: Użytkownik ma dostęp do systemu zarządzania zadaniami
        When: Użytkownik dodaje nowe zadanie o tytule "Napisać raport" i opisie "Przygotować raport miesięczny"
        Then: Zadanie powinno zostać dodane do systemu
        And: Zadanie powinno mieć status "TO_DO"
        And: Zadanie powinno mieć dzisiejszą datę utworzenia
        """
        # Given
        # (kontekst jest już przygotowany w setUp)

        # When
        title = "Napisać raport"
        description = "Przygotować raport miesięczny"
        task_id = self.task_manager.add_task(title, description)

        # Then
        self.assertIsNotNone(task_id, "Zadanie powinno zostać dodane i zwrócić ID")

        # And
        task = self.task_manager.get_task(task_id)
        self.assertEqual(task.title, title, "Tytuł zadania powinien być zgodny z podanym")
        self.assertEqual(task.description, description, "Opis zadania powinien być zgodny z podanym")

        # And
        self.assertEqual(task.status, TaskStatus.TO_DO, "Nowe zadanie powinno mieć status TO_DO")

        # And
        today = datetime.now().date()
        self.assertEqual(task.created_date.date(), today, "Data utworzenia zadania powinna być dzisiejsza")

    def test_marking_task_as_completed(self):
        """
        Scenariusz: Oznaczanie zadania jako ukończone

        Given: Użytkownik ma zadanie o tytule "Zadzwonić do klienta" w systemie
        When: Użytkownik oznacza zadanie jako ukończone
        Then: Status zadania powinien zmienić się na "DONE"
        And: Data ukończenia zadania powinna zostać ustawiona
        """
        # Given
        task_id = self.task_manager.add_task("Zadzwonić do klienta", "Omówić szczegóły projektu")
        task_before = self.task_manager.get_task(task_id)
        self.assertEqual(task_before.status, TaskStatus.TO_DO, "Zadanie wyjściowe powinno mieć status TO_DO")

        # When
        self.task_manager.mark_as_done(task_id)

        # Then
        task_after = self.task_manager.get_task(task_id)
        self.assertEqual(task_after.status, TaskStatus.DONE,
                         "Zadanie powinno mieć status DONE po oznaczeniu jako ukończone")

        # And
        self.assertIsNotNone(task_after.completed_date, "Data ukończenia powinna być ustawiona")
        today = datetime.now().date()
        self.assertEqual(task_after.completed_date.date(), today, "Data ukończenia powinna być dzisiejsza")

    def test_filtering_overdue_tasks(self):
        """
        Scenariusz: Filtrowanie przeterminowanych zadań

        Given: Użytkownik ma kilka zadań w systemie z różnymi terminami
        And: Jedno zadanie ma termin w przeszłości
        And: Jedno zadanie ma termin w przyszłości
        And: Jedno zadanie nie ma ustalonego terminu
        When: Użytkownik filtruje zadania przeterminowane
        Then: Lista powinna zawierać tylko zadanie z terminem w przeszłości
        """
        # Given
        yesterday = datetime.now() - timedelta(days=1)
        tomorrow = datetime.now() + timedelta(days=1)

        # And
        overdue_task_id = self.task_manager.add_task("Przeterminowane zadanie", "To zadanie jest już przeterminowane")
        self.task_manager.set_due_date(overdue_task_id, yesterday)

        # And
        future_task_id = self.task_manager.add_task("Przyszłe zadanie", "To zadanie ma termin w przyszłości")
        self.task_manager.set_due_date(future_task_id, tomorrow)

        # And
        no_due_date_task_id = self.task_manager.add_task("Zadanie bez terminu", "To zadanie nie ma ustalonego terminu")

        # When
        overdue_tasks = self.task_manager.get_overdue_tasks()

        # Then
        self.assertEqual(len(overdue_tasks), 1, "Powinna być tylko jedna przeterminowana zadanie")
        self.assertEqual(overdue_tasks[0].id, overdue_task_id, "Przeterminowane zadanie powinno być na liście")

        # And - dodatkowa weryfikacja
        overdue_task_ids = [task.id for task in overdue_tasks]
        self.assertNotIn(future_task_id, overdue_task_ids, "Zadanie z przyszłym terminem nie powinno być na liście")
        self.assertNotIn(no_due_date_task_id, overdue_task_ids, "Zadanie bez terminu nie powinno być na liście")


if __name__ == '__main__':
    unittest.main()