# Změna zabezpečovacího systému
Začaly jste pracovat v nové firmě a jak už to tak bývá, je potřeba si zvyknout na změnu. Hlavní změna je, že se zde nepoužívají hesla, ale __přístupové fráze__. Např.: `aa bb ced` je __validní__. Aby se zlepšila bezpečnost, chce se zajistit, aby se slova v rámci jedné fráze neopakovala. Tzn. není povoleno: `aa bb cc aa`, jelikož __aa__ se ve frázi vyskytuje 2x.

## Zadání
Ve složce máte k dispozici soubor, kde jsou uloženy __přístupové fráze__ (phrases.txt, každá fráze je oddělena novým řádkem, tzn. `\n`), které už jsou v databázi. Zjistíte, kolik frází zaměstnanci zadali do databáze špatně?

## Jak na to?
1) Zparsovat soubor - řádky si uložit do `ArrayList` nebo do pole. Řádky pak můžete opět rozdělit pomocí metody `split()`.
2) Pro každý řádek zjistit, jestli obsahuje duplicitu. 
3) Pokud obsahuje duplicitu, inkrementovat součet duplicit.

## K zamyšlení
1) Bude nám stačit funkce, nebo chceme použít i objekty?
2) Jak detekovat duplicity v rámci řádků?

## Výsledek pro kontrolu
Soubor __phrases.txt__ obsahuje 57 nevalidních přístupových frází.

## Rozšíření
Šéf si vymyslel, že zabezpečení není dostatečné. Chtěl by, aby mezi nevalidní fráze spadaly i takové, které obsahují slova se stejnými písmeny. 

Např. `abec cab cbae` není validní, protože abec a cbae obsahují stejná písmena. 
Kdežto `abec cab cbaec` už validní je, protože ze slova `abec` různým prohozením písmen slovo `cbaec` neposkládáme.
