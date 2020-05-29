package src.research;

import java.util.*;

import src.research.ZeroPaddings.ArgsZeroPaddingUseClass;
import src.research.callback.*;

public class Main {
    public static void main(String[] args) {
        Timer timer = new Timer();
        Callback callbackInstance = new ZeroPaddings();
        
        // callbackWithHashMap
        HashMap<String, Object> argsCallback = new HashMap<>();
        argsCallback.put("l", 20);
        argsCallback.put("n", 100);
        timer.nanoTimerWithHashMap(callbackInstance, "zeroPadding1_WithHashmap", argsCallback);
        timer.nanoTimerWithHashMap(callbackInstance, "zeroPadding2_WithHashmap", argsCallback);
        
        // callbackFixTypes
        // HashMap<String, Object> argsCallback2 = new HashMap<>();
        // argsCallback2.put("l", new CallbackArg<Integer>(Integer.class, 20));
        // argsCallback2.put("s", new CallbackArg<String>(String.class, "Hello!"));
        // // argsCallback2.put("l", new CallbackArg<Number>(Integer.class, 20.0)); // エラー
        // timer.nanoTimerFixTypes(callbackInstance, "zeroPadding1_FixTypes", argsCallback2);

        // callbackUseClass
        timer.nanoTimerUseClass(
            callbackInstance,
            "zeroPadding1_UseClass",
            new ArgsZeroPaddingUseClass(20, 100));
    }
}


