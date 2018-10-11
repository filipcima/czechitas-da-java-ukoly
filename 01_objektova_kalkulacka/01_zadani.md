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
- V teto metode sectete dve cisla, vysledek ulozte do promenne vysledek.
### public double odcitani()
- Odectete dve cisla, vysledek ulozte do promenne vysledek.
### public double nasobeni()
- V teto metode... (viz. vyse)
### public double deleni()
- Vysledek ulozte do promenne vysledek, ale pozor na deleni nulou! Osetrete podminkou - pokud nekdo bude chtit delit nulou, vypiste do konzole "Delit nulou nelze!".
### public double vratVysledek()
- Tahle metoda pouze vrati vysledek z promenne vysledek.
- Zkuste zapremyslet, co se asi stane, kdyz zavolate tuto metodu predtim nez provedete jednu z operaci (soucet, deleni, nasobeni, odcitani).

## Funkcionalita
```java
public static void main() {
	Kalkulacka kalkulacka = new Kalkulacka(3, 5);
	double soucet = kalkulacka.soucet(); // soucet = 8
	double vysledek = kalkulacka.vratVysledek(); // vysledek = 8
}
```
## Napad na rozsireni
1) V metode main nacitejte hodnoty v cyklu jako u prvniho ukolu Stepana.
2) Pretizte nebo upravte metodu vratVysledek tak, aby prijimala jeden argument String __oprace__ a na zaklade toho se rozhodne, ktera operace se zavola.
```java
public static void main() {
	Kalkulacka kalkulacka = new Kalkulacka(2, 4);
	double vysledek = kalkulacka.vratVysledek("*"); // vysledek = 8
	vysledek = kalkulacka.vratVysledek("-") // vysledek = -2
}
```
Pro rozpoznani operace pouzijte podminky a `operace.equals("-")`.
