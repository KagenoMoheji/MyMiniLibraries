package src.samples.method2;

import src.samples.method2.ZeroPaddings.ArgsZeroPadding;
import src.samples.method2.callback.*;

public class Main {
    public static void main(String[] args) {
        Timer timer = new Timer();
        Callback callbackInstance = new ZeroPaddings();

        timer.nanoTimer(
            callbackInstance,
            "zeroPadding1",
            new ArgsZeroPadding(20, 100));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding2",
            new ArgsZeroPadding(20, 100));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding3",
            new ArgsZeroPadding(20, 100));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding4",
            new ArgsZeroPadding(20, 100));
        
        // ArgsZeroPadding a = new ArgsZeroPadding(20, 100);
        // System.out.println(a.getN()); // スコープエラー
    }
}


