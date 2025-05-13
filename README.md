# Task Manager pro testovací účely

*Note: English follows*

Jednoduchý task manager v Pythonu, který slouží jako základ k vytvoření testovacích scénářů.

## Popis

Program umožňuje uživateli přidávat, zobrazovat a odstraňovat úkoly.

Jednotlivé funkce:
*   přidání úkolu
*   zobrazení všech úkolů
*   odstranění úkolu
*   ošetření neplatného vstupu uživatele
*   ošetření prázdného názvu úkolu a popisu
*   ošetření prázdného seznamu úkolů
*   ošetření neplatného čísla úkolu při odstraňování

## Použité knihovny a verze Pythonu

Tento program vyžaduje **Python 3.9** a novější.

Nejsou vyžadování žádné externí knihovny.

## Používání programu

Program spustíte přímo z příkazového řádku příkazem `python main.py`.
Všechny ostatní vstupy se zadávají v příkazovém řádku a potvrzují se klávesou Enter.
Uživatel postupuje podle instrukcí v konzoli. Zvolí si akci, zadá odpovídající číslo a potvrdí.

## Příklad fungování

Spuštění:

`python main.py`

Ukázka:

```
Správce úkolů – Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1–4): 1

Zadejte název úkolu: Úkol 1
Zadejte popis úkolu: popis k úkolu 1
Úkol 'Úkol 1' byl přidán.

Hlavní menu
...
Vyberte možnost (1–4): 3   

Seznam úkolů:
1. Úkol 1 – popis k úkolu 1

Zadejte číslo úkolu, který chcete odstranit: 1
Úkol 'Úkol 1' byl odstraněn.
```

## Autor
Štěpán Pala


# Task Manager for testing purposes

A simple task manager in Python that serves as a basis for creating test scenarios.

## Description

The program allows the user to add, view and delete tasks.

Functions:
*   add a task
*   view all tasks
*   remove a task
*   handling invalid user input
*   handling empty task name and description
*   handling an empty task list
*   handling an invalid task number when deleting

## Dependencies

This program requires **Python 3.9** or newer.

No external libraries required.

## Usage

Execute the script directly from your terminal/command line using `python main.py`.
All other inputs are typed in the command line and confirmed with the Enter key.
Follow the instructions in the command line. Choose an action, enter the corresponding number and confirm.

## Example

Execution:

`python main.py`

Example:
Note: The actual program interface and output are in Czech. The example below is translated for clarity.

```
Task Manager – Main Menu
1. Add New Task
2. View All Tasks
3. Remove Task
4. End Program
Select an option (1–4): 1

Enter Task name: Task 1
Enter Task description: task description 1
Task 'Task 1' has been added.

Main Menu
...
Select an option (1–4): 3

Task List:
1. Task 1 – task description 1

Enter the number of task you wish to remove: 1
Task 'Task 1' has been removed.
```

## Author
Štěpán Pala
