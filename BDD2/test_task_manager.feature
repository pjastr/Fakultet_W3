Feature: Zarządzanie zadaniami

  Scenario: Dodawanie nowego zadania
    Given a task manager is available
    When the user adds a new task with title "Napisać raport" and description "Przygotować raport miesięczny"
    Then the task should exist in the system with title "Napisać raport" and description "Przygotować raport miesięczny"

  Scenario: Oznaczanie zadania jako ukończone
    Given a task with title "Zadzwonić do klienta" and description "Omówić szczegóły projektu" exists
    When the user marks the task as done
    Then the task status should be DONE and completed_date is set

  Scenario: Filtrowanie przeterminowanych zadań
    Given multiple tasks exist with various due dates
    When the user filters overdue tasks
    Then only the overdue task is returned
