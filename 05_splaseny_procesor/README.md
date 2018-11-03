# Splašený procesor

Je potřeba rychlého jednání! Procesor uvíznul v bludišti instrukcí a potřebuje pomoc od jakéhokoli programu, který mu pomůže se z bludiště vymotat.

## Zadání
V souboru `instructions.txt` je seznam "offsetů" pro každý skok. Skoky jsou relativní: -1 skočí na předchozí instrukci a číslo 3 skočí z aktuálního místa o 3 instrukce vpřed. Začínáte na první instrukci v listu. Cílem je zpracovávat instrukce, dokud nevyskočíte z pole instrukcí pryč.

Aby to nebylo úplně jednoduché, instrukce jsou tak trochu podivné - po každém skoku se instrukce, ze které skáčete inkrementuje o 1. Takže když budete na instrukci s hodnotou 3, posunete se o 3 vpřed, ale číslo 3 z políčka, kde jste stály, se změní na 4.

Zjistěte, __kolik skoků__ bude potřeba k opuštění bludiště.

## Příklad:
Pro ilustraci vezměme v potaz následující seznam "offsetů":
```
 0
 3
 0
 1
-3
```
- Kladná čísla: posunutí "vpřed"
- Záporná čísla: posunutí "vzad"

Pro přehlednost si čísla dáme do řádku a v závorkách bude číslo, na kterém se právě nacházíme.

- `_(0)_3__0__1__-3__`- __výchozí stav__ - ještě jsme neudělali ani jeden skok
- `_(1)_3__0__1__-3__`- __skok s offsetem 0__ - (skočíme na místě) - naštěstí, offset se inkrementoval o jedničku
- `__2_(3)_0__1__-3__`- __skok vpřed o 1__ - ale musíme inkrementovat číslo, ze kterého jsme skákali
- `__2__4__0__1_(-3)_`- __skok o 3__ znamená posun až na konec a za sebou necháme číslo 4
- `__2_(4)_0__1__-2__`- __skok o -3__? to je tam, kde jsme právě byli! z -3 je rázem -2
- `__2__5__0__1__-2__`- __skok o 4 vpřed__ - jsme venku!

Opustit bludiště zabralo 5 skoků.

## Výsledek
Opustit poněkud větší bludiště ze zadání zabere __360603 skoků__.
