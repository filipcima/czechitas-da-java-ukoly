package com.company;

public enum Smer {
    SEVER,
    VYCHOD,
    JIH,
    ZAPAD;

    public Smer next() {
        try {
            return values()[ordinal() + 1];
        } catch (ArrayIndexOutOfBoundsException e) {
            return values()[0];
        }

    }

    public Smer prev() {
        try {
            return values()[ordinal() - 1];
        } catch (ArrayIndexOutOfBoundsException e) {
            return values()[values().length - 1];
        }

    }
}
