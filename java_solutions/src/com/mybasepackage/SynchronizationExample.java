package com.mybasepackage;


class Table {
    synchronized void printTable(int n) {
        // method not synchronized
        for (int i=0; i<5; i++) {
            System.out.println(i*n);
        }
        try{
            Thread.sleep(400);
        } catch (Exception e) {
            System.out.println(String.format("Exception caught! Details: ", e));
        }
    }
}

class ThreadOne extends Thread {
    Table t;
    ThreadOne(Table _t) {
        this.t = _t;
    }
    public void run() {
        t.printTable(5);
    }
}

class ThreadTwo extends Thread {
    Table t;
    ThreadTwo(Table _t) {
        this.t = _t;
    }
    public void run() {
        t.printTable(100);
    }
}


public class SynchronizationExample {

    public static void main(String[] args) {
        Table newTable = new Table();
        new Thread() {
            public void run() {
                newTable.printTable(3);
            }
        }.start();
        ThreadOne tOne = new ThreadOne(newTable);
        ThreadTwo tTwo = new ThreadTwo(newTable);
        tOne.start();
        tTwo.start();
    }
}
