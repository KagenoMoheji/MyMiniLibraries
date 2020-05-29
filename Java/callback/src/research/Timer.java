package src.research;

import java.util.*;

import src.research.callback.*;

public class Timer {
    public void nanoTimerWithHashMap(Callback callbackInstance, String methodName, HashMap<String, Object> args) {
        double start = System.nanoTime();
        callbackInstance.callbackWithHashmap(methodName, args);
        System.out.println((System.nanoTime() - start) / 1__000__000__000);
    }

    public void nanoTimerFixTypes(Callback callbackInstance, String methodName, HashMap<String, Object> args) {
        double start = System.nanoTime();
        callbackInstance.callbackFixTypes(methodName, args);
        System.out.println((System.nanoTime() - start) / 1__000__000__000);
    }

    public void nanoTimerUseClass(Callback callbackInstance, String methodName, ArgsUseClassInterface args) {
        double start = System.nanoTime();
        callbackInstance.callbackUseClass(methodName, args);
        System.out.println((System.nanoTime() - start) / 1__000__000__000);
    }
}