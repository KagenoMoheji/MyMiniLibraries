package src.samples.method2;

import src.samples.method2.callback.*;
import src.samples.method2.ZeroPaddings.ArgsZeroPadding;
import src.samples.method2.ZeroPaddings.ArgsTestCannotBeCalled;

public class Main {
    public static void main(String[] args) {
        Timer timer = new Timer();
        Callback callbackInstance = new ZeroPaddings();

        timer.nanoTimer(
            callbackInstance,
            "zeroPadding1",
            new ArgsZeroPadding(20, 1020553));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding2",
            new ArgsZeroPadding(20, 1020553));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding3",
            new ArgsZeroPadding(20, 1020553));
        timer.nanoTimer(
            callbackInstance,
            "zeroPadding4",
            new ArgsZeroPadding(20, 1020553));
        
        // 内部クラス(コールバックの引数定義クラス)のメソッドのスコープエラー
        // ArgsZeroPadding a = new ArgsZeroPadding(20, 100);
        // System.out.println(a.getN());

        // Callbackを実装したクラスにおける@CallbackMethoが付いていないpublicメソッドを呼び出せないエラー
        // timer.nanoTimer(
        //     callbackInstance,
        //     "testCannotBeCalledPublicWithoutAnnotation",
        //     new ArgsTestCannotBeCalled(5, 6));

        // Callbackを実装したクラスにおけるprivateメソッドを呼び出せないエラー
        // publicにした場合は，戻り値のあるcallbackの挙動テスト
        // timer.nanoTimerWithCallbackHasReturn(
        //     callbackInstance,
        //     "testCannotBeCalledPrivate",
        //     new ArgsTestCannotBeCalled(5, 6));
    }
}


