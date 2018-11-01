# Santovo cestování
Havarovali jste spolu se Santou ve městě, bohužel elfí kočí omdlel a nejde ho vzbudit. Není čas zastavovat v nemocnici, protože dárky se samy nerozvezou. Naštěstí má Santa po ruce tebe a elfí deník, kde instrukce pro soby jsou. Jsou ale dost pomatené a nemáte moc času. Zjisti, kolik bloků nejméně budete se Santou muset ujet, abyste se dostali do cíle. 

## Zadání
Instrukce jsou ve tvaru `směr(L/R)počet bloků` - např `L2`. Kočár začíná otočen na __sever__. L2 znamená otočení na západ, pokud jsme předtím byli otočení na sever. Číslo 2 znamená - posuň se o dva bloky rovně. 

`R5` znamená otočení o 90 stupňů doprava (pokud kočár směřoval na západ, otočíme se na sever) a 5 bloků vpřed. `R2, L3`

Ve složce máte k dispozici soubor __instrukce.txt__, ktery si načtete a budete procházet instrukce. Po zpracování všech instrukcí se dostanete na určené místo. Santu ale zajímá, jaká je nejkratší cesta do cíle. Doporučuji se podívat na [Manhattanskou metriku](https://cs.wikipedia.org/wiki/Manhattansk%C3%A1_metrika). Zadávejte souřadnice do [kartézské soustavy souřadnic](https://cs.wikipedia.org/wiki/Kart%C3%A9zsk%C3%A1_soustava_sou%C5%99adnic).

## Příklad
- soubor obsahuje: `R2, R2, R2` - vždy je vychozí směr __sever__ , otočíme se doprava (na vychod) a pojedeme dva bloky rovně. Nyní se nacházíme 2 bloky severně od vychozí pozice. v druhém kroku se otočíme opět doprava (budeme směřovat na jih) a pojedeme dva bloky vpřed. Nyní jsme 4 bloky od vychozí pozice. V posledním kroku se otočíme opět doprava (směrem na západ) a ujedeme dva bloky. Nyní jsme ujeli 6 bloků, ale nejkratší cesta z vychozího bodu do cíle je 2 bloky. __Zkuste si to nakreslit!__ 
- `R5, L5, R5, R3` - vychozí směr: __sever__. Otočíme se doprava, ujedeme 5 bloků rovně. Otočíme se doleva, popojedeme o 5 bloků rovně. Otočíme se doprava, ujedeme opět 5 bloků. V poslední řadě se otočíme doprava a ujedeme tři bloky. Jaká je nejkratší vzdálenost z vychozího bodu do cíle? Správná odpověď je 12. __Opět zkuste nakreslit, abyste to lépe pochopily.__

## Jak na to?
- Základem je __zparsovat__ soubor: Vytvořil bych si ArrayList nebo pole stringů, kde prvkem bude instrukce např `"L2"`.
- Pak bych procházel pole nebo ArrayList a podle toho, kterym směrem jsme otočení, na té ose se posuneme buď do kladnych, nebo zapornych cisel
- Hodit se budou proměnné:
```java
int aktualniPoziceX = 0;
int aktualniPoziceY = 0;
int smer = 0;
```
Jestli vás mate, že je směr číslo, tak nemusí. Představte si, že když je směr 0 sever a v instrukci máte písmeno L - otočíme se na západ. Směr bude -1. Pokud se poté otočíme zase doleva, bude to -2. Pokud bychom takhle pokračovali i dále, mohli bychom se dostat do situace, kde směr bude třeba -40. To nechceme. Zkuste se podívat na operátor modulo - zbytek po dělení (%).

## Řešení
Číslo __298__ je správná odpověď. 
