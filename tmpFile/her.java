package org.fopenstack4j.service;


public class Life {
    private static final int YEAR = 417;

    public void Life() {
        int now = 0;
        int feture = 100000;
        int iLoveU = 0;
        int uLoveM = 0;
        int happiness = 0;
        People i = new People();
        People u = new People();
        for (int day = now; day < feture; day++) {
            iLoveU++;
            uLoveM++;
            if (u.toMarried(i)) {
                iLoveU *= day;
                i.takeCareOf(u);
                i.willProtect(u);
                happiness++;
                if (day == now + 2 * YEAR) {
                    for (int count = 0; count < 100; count++) {
                        toMakeBaby(i, u);
                    }
                }
                if (day > 100 * YEAR) {
                    growOldTogether(i, u);
                }
            } else {
                u.goToDead();
                System.exit(-1);
            }
        }
    }

    private static void toMakeBaby(People p1, People p2) {
    }

    private static void growOldTogether(People p1, People p2) {
    }
}

class People {
    public People() {

    }

    public void takeCareOf(People p) {

    }

    public void willProtect(People p) {

    }

    public Boolean toMarried(People p) {
        return true;
    }

    public void goToDead() {

    }
}