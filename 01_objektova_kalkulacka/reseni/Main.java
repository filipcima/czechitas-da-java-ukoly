package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        do {
            double cislo1, cislo2, vysledek;
            String operace;

            System.out.print("Zadej vstup: ");
            operace = sc.nextLine();

            if (operace.equals("konec")) {
                System.out.println("Zadan konec.");

                break; // ukonci cyklus
            }

            if (!operace.equals("+") && !operace.equals("-") && !operace.equals("*") && !operace.equals("/")) {
                System.out.println("Zadan spatny vstup.");
                continue; // dostane se na zacatek cyklu dalsi iterace
            }

            System.out.print("Zadejte cislo 1: ");
            cislo1 = sc.nextDouble();
            sc.nextLine();

            System.out.print("Zadejte cislo 2: ");
            cislo2 = sc.nextDouble();
            sc.nextLine();

            Kalkulacka kalkulacka = new Kalkulacka(cislo1, cislo2);
            vysledek = kalkulacka.vratVysledek(operace);
            System.out.println(vysledek);
        } while (true);
        sc.close();

    }
}

