package com.company;

public class Kalkulacka {
    private double cislo1;
    private double cislo2;
    private double vysledek;

    public Kalkulacka(double cislo1, double cislo2) {
        this.cislo1 = cislo1;
        this.cislo2 = cislo2;
    }

    private double odcitani() {
        this.vysledek = this.cislo1 - this.cislo2;
        return vysledek;
    }

    private double scitani() {
        this.vysledek = this.cislo1 + this.cislo2;
        return vysledek;
    }

    private double nasobeni() {
        this.vysledek = this.cislo1 * this.cislo2;
        return vysledek;
    }

    private double deleni() {
        if (this.cislo2 == 0) {
            System.out.println("Delit nulou nelze!");
            return 0;
        }
        this.vysledek = this.cislo1 / this.cislo2;
        return vysledek;
    }

    public double vratVysledek(String operace) {
        if (operace.equals("+")) {
            return scitani();
        } else if (operace.equals("-")) {
            return odcitani();
        } else if (operace.equals("*")) {
            return nasobeni();
        } else if (operace.equals("/")) {
            return deleni();
        } else {
            return vysledek;
        }
    }
}
