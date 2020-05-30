package src.samples.method2;

import src.samples.method2.ZeroPaddings.ArgsZeroPaddingUseClass;
import src.samples.method2.callback.*;

public class Main {
    public static void main(String[] args) {
        Timer timer = new Timer();
        Callback callbackInstance = new ZeroPaddings();

        timer.nanoTimer(
            callbackInstance,
            "zeroPadding1",
            new ArgsZeroPaddingUseClass(20, 100));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding2",
            new ArgsZeroPaddingUseClass(20, 100));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding3",
            new ArgsZeroPaddingUseClass(20, 100));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding4",
            new ArgsZeroPaddingUseClass(20, 100));
        
        // ArgsZeroPaddingUseClass a = new ArgsZeroPaddingUseClass(20, 100);
        // System.out.println(a.getN()); // スコープエラー
    }
}


