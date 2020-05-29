package src.samples.method1;

import java.util.*;

import src.samples.method1.callback.*;

public class Main {
    public static void main(String[] args) {
        Timer timer = new Timer();
        Callback callbackInstance = new ZeroPaddings();
        
        try {
            HashMap<String, Object> argsCallback = new HashMap<>();
            argsCallback.put("l", 20);
            argsCallback.put("n", 100);
            timer.nanoTimer(callbackInstance, "zeroPadding1", argsCallback);
            timer.nanoTimer(callbackInstance, "zeroPadding2", argsCallback);
            timer.nanoTimer(callbackInstance, "zeroPadding3", argsCallback);
            timer.nanoTimer(callbackInstance, "zeroPadding4", argsCallback);
        } catch(Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
        
    }
}


