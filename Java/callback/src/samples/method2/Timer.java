package src.samples.method2;

import src.samples.method2.callback.*;
import src.samples.method2.callback.annotations.CallerMethod;
import src.samples.method2.callback.exceptions.CannotRunPrivateCallbackException;
import src.samples.method2.callback.exceptions.NoAnnotationException;

public class Timer {
    @CallerMethod
    public void nanoTimer(Callback callbackInstance, String methodName, CallbackArgsInterface args) {
        try { // NoAnnotationExceptionのためのtry-catch必要
            double start = System.nanoTime();
            // ここでコールバックメソッド実行
            callbackInstance.callback(methodName, args);
            System.out.println((System.nanoTime() - start) / 1__000__000__000);
            System.out.println("--------------------------------");
        } catch(NoAnnotationException | CannotRunPrivateCallbackException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }

    @CallerMethod
    public void nanoTimerWithCallbackHasReturn(Callback callbackInstance, String methodName, CallbackArgsInterface args) {
        try { // NoAnnotationExceptionのためのtry-catch必要
            double start = System.nanoTime();
            // ここでコールバックメソッド実行
            int res = (int)callbackInstance.callbackHasReturn(methodName, args);
            System.out.println(res);
            System.out.println((System.nanoTime() - start) / 1__000__000__000);
            System.out.println("--------------------------------");
        } catch(NoAnnotationException | CannotRunPrivateCallbackException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}