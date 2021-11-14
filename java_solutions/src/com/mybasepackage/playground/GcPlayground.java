package com.mybasepackage.playground;

import java.awt.*;

public class GcPlayground {
    GcPlayground ptr;

    public static void main(String[] args) {
        System.out.println("Hello from GcPlayground!");

        GcPlayground a = new GcPlayground();
        GcPlayground b = new GcPlayground();
        a.ptr = b;
        b.ptr = a;

        System.out.println("Hello from GcPlayground!");
        System.gc();

        a = null;

        System.gc();
        b = null;

        System.gc();
    }

   @Override
   protected void finalize() throws Throwable{
      System.out.println("The finalize method has been called on the object");
   }
}