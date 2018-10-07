# Objektove orientovana kalkulacka

## Zadani
Vytvorte tridu Kalkulacka, ktera nam bude slouzit pro scitani/odcitani/deleni/nasobeni dvou cisel.

Objekt bude mit tri atributy:
- private double __cislo1__
- private double __cislo2__
- private double __vysledek__

Konstruktor bude obsahovat dva parametry:
- double ___cislo1__
- double ___cislo2__
V tele konstruktoru je nastavte do promennych vasi tridy.

__Do tridy pridejte 5 metod:__
### public double soucet()
- v teto metode sectete dve cisla, vysledek ulozte do promenne vysledek a vratte jejich vysledek.
### public double odcitani()
- v teto metode odectete dve cisla, vysledek ulozte do promenne vysledek a vratte jejich vysledek.
### public double nasobeni()
- v teto metode... (viz. vyse)
### public double deleni()
- vratte vysledek deleni dvou cisel, vysledek ulozte do promenne vysledek, ale pozor na deleni nulou! Osetrete podminkou - pokud nekdo bude chtit delit nulou, vypiste do konzole "Delit nulou nelze!" a vratte 0.
### public void vypisVysledek()
- tahle metoda bude vypisovat neco ve stylu "3 + 3 = 6".

## Funkcionalita
```java
public static void main() {
	Kalkulacka kalkulacka = new Kalkulacka(3, 5);
	double soucet = kalkulacka.soucet(); // soucet = 8
	kalkulacka.vypisVysledek(); // "3 + 5 = 8"
}
```
## Napad na rozsireni
V metode main nacitejte hodnoty v cyklu jako u prvniho ukolu Stepana.
