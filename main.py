"""
Jednoduchý správce úkolů v Pythonu.
Slouží jako podklad k vytvoření testovacích případů.
Tento skript umožňuje uživateli přidávat, zobrazovat a odstraňovat úkoly.
"""

def hlavni_menu() -> str:
    """Zobrazí hlavní menu a vrátí volbu uživatele."""
    print("\nSprávce úkolů – Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    volba_uzivatele = input("Vyberte možnost (1–4): ")
    return volba_uzivatele


def pridat_ukol():
    """Přidá nový úkol do seznamu úkolů."""
    nazev_ukolu = input("\nZadejte název úkolu: ")
    popis_ukolu = input("Zadejte popis úkolu: ")
    # Přidání úkolu do seznamu jako slovník
    ukoly.append({"název": nazev_ukolu, "popis": popis_ukolu})
    print(f"Úkol '{nazev_ukolu}' byl přidán.")


def zobrazit_ukoly():
    """Zobrazí všechny úkoly v seznamu."""
    print("\nSeznam úkolů:")
    # Projítí seznamu úkolů a vypsání každého úkolu s jeho indexem
    for index, task in enumerate(ukoly):
        print(f"{index + 1}. {task['název']} – {task['popis']}")


def odstranit_ukol() :
    """Odstraní úkol ze seznamu."""
    cislo_ukolu = input("\nZadejte číslo úkolu, který chcete odstranit: ")
    # Výběr úkolu podle indexu (uživatelský vstup je 1-based, seznam je 0-based)
    index = int(cislo_ukolu) - 1
    odstraneny_ukol = ukoly.pop(index)
    print(f"Úkol '{odstraneny_ukol['název']}' byl odstraněn.")


# Globální proměnná pro ukládání úkolů (seznam slovníků)
ukoly: list[dict[str, str]] = []


# Hlavní část programu, která se spouští při spuštění skriptu
if __name__ == "__main__":
    # Nekonečná smyčka zobrazující menu, dokud uživatel nezvolí konec programu
    while True:
        # Získání volby od uživatele
        volba = hlavni_menu()
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            # Ukončení programu
            print("Konec programu.")
            break # Konec smyčky
