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

Správce úkolů – Hlavní menu
1. Přidat nový úkol        
2. Zobrazit všechny úkoly  
3. Odstranit úkol
4. Konec programu
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

Initiation:

`python main.py`

Example:

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

Správce úkolů – Hlavní menu
1. Přidat nový úkol        
2. Zobrazit všechny úkoly  
3. Odstranit úkol
4. Konec programu
Vyberte možnost (1–4): 3   

Seznam úkolů:
1. Úkol 1 – popis k úkolu 1

Zadejte číslo úkolu, který chcete odstranit: 1
Úkol 'Úkol 1' byl odstraněn.
```

## Author
Štěpán Pala
