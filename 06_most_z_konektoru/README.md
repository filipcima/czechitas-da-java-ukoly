#  Most z konektorů

Procesor je sám o sobě obrovská černá budova obklopena bezednou jámou. Obrovské kovové trubky vyčnívají ze stran budovy v pravidelných intervalech směrem ven. Neexistuje žádný způsob, jak je překročit, ale musíte se dostat dovnitř.

Tedy existuje způsob - postavit __most z magnetických komponent__, které jsou pohozeny poblíž.

## Zadání

Každá komponenta má 2 porty - na konci a na začátku. Je spousta typu portů, ale můžete propojit pouze odpovídající typy, aby do sebe hezky zapadly. Každý port je identifikován pomocí počtu pinů - viz. __input.txt__. (Na jednom řádku jedna magnetická komponenta - počet pinů na jednom konci/počet pinů na druhém konci)

Pro ilustraci: `3/7` komponenta má na jednom konci 3 piny a na druhém 7 pinů.

Vaše strana jámy je metalická, takže je úplně ideální pro připojení komponenty, která má na jedné straně __0 pinů__ - hezky k metalické zdi přilne. Proto musíte začít právě touto komponentou.

__Síla mostu__ je definována jako součet všech portů všech komponent.

Např.: Pokud se most bude skládat z komponent `0/3`, `3/7`, a `7/4`, tak __síla mostu__ bude `0+3 + 3+7 + 7+4 = 24`.

__Jaký nejpevnější most dokážete postavit ze součástek ze zadání?__

## Příklad
Máte k dispozici tyto komponenty:
```
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
```

Z těchto můžete poskládat následující validní mosty:
- `0/1`
- `0/1`--`10/1`
- `0/1`--`10/1`--`9/10`
- `0/2`
- `0/2`--`2/3`
- `0/2`--`2/3`--`3/4`
- `0/2`--`2/3`--`3/5`
- `0/2`--`2/2`
- `0/2`--`2/2`--`2/3`
- `0/2`--`2/2`--`2/3`--`3/4`
- `0/2`--`2/2`--`2/3`--`3/5`

Všimněte si (na třetí kombinaci), že u portů nezáleží na pořadí: Na komponentu `0/1` můžeme napasovat `10/1`, jelikož na jednom konci jednička je, ale musíme vzít potaz, že když komponentu obrátíme, musíme k ní dopasovat něco s desítkou. V tomto případě `9/10`.

Z těchto mostů je nejpevnější tento: `0/1`--`10/1`--`9/10`; Jeho síla je 31.

## Rady k zadání
Zatím žádné.

## Výsledek
Největší možná síla mostu z komponent je 1859.