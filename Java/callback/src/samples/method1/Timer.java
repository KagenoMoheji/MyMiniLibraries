package src.samples.method1;

import java.util.*;

import src.samples.method1.callback.*;

public class Timer {
    // Caller Method
    public void nanoTimer(Callback callbackInstance, String methodName, HashMap<String, Object> args) {
        double start = System.nanoTime();
        // ここでコールバックメソッド実行
        callbackInstance.callback(methodName, args);
        System.out.println((System.nanoTime() - start) / 1__000__000__000);
        System.out.println("--------------------------------");
    }
}