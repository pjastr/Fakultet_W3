from datetime import datetime, timedelta
import pytest
from pytest_bdd import scenario, given, when, then, parsers
from task_manager import TaskManager, TaskStatus

# Scenariusze (odwołują się do pliku .feature)
@scenario("test_task_manager.feature", "Dodawanie nowego zadania")
def test_adding_new_task():
    pass

@scenario("test_task_manager.feature", "Oznaczanie zadania jako ukończone")
def test_marking_task_as_done():
    pass

@scenario("test_task_manager.feature", "Filtrowanie przeterminowanych zadań")
def test_filtering_overdue_tasks():
    pass


# Fixture
@pytest.fixture
def task_manager():
    return TaskManager()


# Scenario: Dodawanie nowego zadania
@given("a task manager is available")
def given_task_manager(task_manager):
    return task_manager

@when(parsers.parse('the user adds a new task with title "{title}" and description "{description}"'), target_fixture="task_id")
def add_new_task(task_manager, title, description):
    return task_manager.add_task(title, description)

@then(parsers.parse('the task should exist in the system with title "{expected_title}" and description "{expected_description}"'))
def check_new_task(task_manager, task_id, expected_title, expected_description):
    task = task_manager.get_task(task_id)
    assert task is not None, "Zadanie nie zostało dodane"
    assert task.title == expected_title, "Niepoprawny tytuł zadania"
    assert task.description == expected_description, "Niepoprawny opis zadania"
    assert task.status == TaskStatus.TO_DO, "Nowe zadanie powinno mieć status TO_DO"
    today = datetime.now().date()
    assert task.created_date.date() == today, "Data utworzenia powinna być dzisiejsza"


# Scenario: Oznaczanie zadania jako ukończone
@given(parsers.parse('a task with title "{title}" and description "{description}" exists'), target_fixture="existing_task_id")
def create_task(task_manager, title, description):
    return task_manager.add_task(title, description)

@when("the user marks the task as done", target_fixture="done_task_id")
def mark_task_done(task_manager, existing_task_id):
    task_manager.mark_as_done(existing_task_id)
    return existing_task_id

@then("the task status should be DONE and completed_date is set")
def check_task_done(task_manager, done_task_id):
    task = task_manager.get_task(done_task_id)
    assert task.status == TaskStatus.DONE, "Zadanie nie ma statusu DONE"
    assert task.completed_date is not None, "Data ukończenia nie została ustawiona"
    today = datetime.now().date()
    assert task.completed_date.date() == today, "Data ukończenia powinna być dzisiejsza"


# Scenario: Filtrowanie przeterminowanych zadań
@given("multiple tasks exist with various due dates", target_fixture="tasks_ids")
def create_multiple_tasks(task_manager):
    yesterday = datetime.now() - timedelta(days=1)
    tomorrow = datetime.now() + timedelta(days=1)
    overdue_task_id = task_manager.add_task("Przeterminowane zadanie", "To zadanie jest przeterminowane")
    task_manager.set_due_date(overdue_task_id, yesterday)
    future_task_id = task_manager.add_task("Przyszłe zadanie", "To zadanie nie jest przeterminowane")
    task_manager.set_due_date(future_task_id, tomorrow)
    no_due_date_task_id = task_manager.add_task("Zadanie bez terminu", "To zadanie nie ma ustalonego terminu")
    return {"overdue": overdue_task_id, "future": future_task_id, "none": no_due_date_task_id}

@when("the user filters overdue tasks", target_fixture="overdue_tasks")
def filter_overdue_tasks(task_manager):
    return task_manager.get_overdue_tasks()

@then("only the overdue task is returned")
def check_overdue_tasks(tasks_ids, overdue_tasks):
    assert len(overdue_tasks) == 1, "Liczba przeterminowanych zadań jest niepoprawna"
    assert overdue_tasks[0].id == tasks_ids["overdue"], "Przeterminowane zadanie nie zostało zwrócone"
