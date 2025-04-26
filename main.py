"""
Jednoduchý správce úkolů v Pythonu.
Slouží jako podklad k vytvoření testovacích případů.
Tento skript umožňuje uživateli přidávat, zobrazovat a odstraňovat úkoly.
Základní funkce:
- přidání úkolu
- zobrazení všech úkolů
- odstranění úkolu
- ošetření neplatného vstupu uživatele
- ošetření prázdného názvu úkolu a popisu
- ošetření prázdného seznamu úkolů
- ošetření neplatného čísla úkolu při odstraňování
"""

def hlavni_menu() -> str:
    """
    Zobrazí hlavní menu a vrátí volbu uživatele.
    Uživatel si může vybrat mezi přidáním úkolu, zobrazením úkolů,
    odstraněním úkolu nebo ukončením programu.
    Funkce zajišťuje, že uživatel zadá platnou volbu (1-4).
    Pokud uživatel zadá neplatnou volbu, zobrazí se chybová hláška.

    Returns:
        str: Řetězec reprezentující volbu uživatele (1-4).
    """
    print("\nSprávce úkolů – Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    while True:
        volba_uzivatele = input("Vyberte možnost (1–4): ")
        if volba_uzivatele in ["1", "2", "3", "4"]:
            break # Platná volba, ukončení smyčky
        print("\nNeplatná volba. Zadejte číslo mezi 1 a 4.")
    return volba_uzivatele


def pridat_ukol():
    """
    Přidá nový úkol do seznamu úkolů.
    Uživatel musí zadat název a popis úkolu.
    Funkce zajišťuje, že uživatel zadá název a popis úkolu.
    Pokud uživatel nezadá název nebo popis, zobrazí se chybová hláška.
    """
    while True:
        nazev_ukolu = input("\nZadejte název úkolu: ").strip()
        if nazev_ukolu:
            break
        print("Název úkolu nesmí být prázdný.")

    while True:
        popis_ukolu = input("Zadejte popis úkolu: ").strip()
        if popis_ukolu:
            break
        print("\nPopis úkolu nesmí být prázdný.")

    # Přidání úkolu do seznamu jako slovník
    ukoly.append({"název": nazev_ukolu, "popis": popis_ukolu})
    print(f"Úkol '{nazev_ukolu}' byl přidán.")


def zobrazit_ukoly():
    """
    Zobrazí všechny úkoly v seznamu, případně upozornění, pokud je prázdný.
    """
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for index, task in enumerate(ukoly):
        print(f"{index + 1}. {task['název']} – {task['popis']}")


def odstranit_ukol() :
    """Odstraní úkol ze seznamu.
    Uživatel musí zadat číslo úkolu, který chce odstranit.
    Funkce zajišťuje, že uživatel zadá platné číslo úkolu.
    Pokud uživatel zadá neplatný vstup, zobrazí se chybová hláška.
    """
    if not ukoly:
        print("\nŽádné úkoly k odstranění.")
        return

    while True:
        zobrazit_ukoly()
        try:
            cislo_ukolu = int(
                input("\nZadejte číslo úkolu, který chcete odstranit: ")
            )
            if 1 <= cislo_ukolu <= len(ukoly):
                index = cislo_ukolu - 1
                odstraneny_ukol = ukoly.pop(index)
                print(f"Úkol '{odstraneny_ukol['název']}' byl odstraněn.")
                break # Úspěšné odstranění úkolu, ukončení smyčky

            if len(ukoly) == 1:
                print("Číslo úkolu musí být 1.")
            else:
                print(f"Číslo úkolu musí být mezi 1 a {len(ukoly)}.")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo úkolu.")


# Globální proměnná pro ukládání úkolů (seznam slovníků)
ukoly: list[dict[str, str]] = []


if __name__ == "__main__":
    while True:
        volba = hlavni_menu()
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break # Konec smyčky
