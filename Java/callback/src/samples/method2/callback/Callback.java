package src.samples.method2.callback;

import java.lang.reflect.*;

import src.samples.method2.callback.annotations.CallbackMethod;
import src.samples.method2.callback.exceptions.CannotRunPrivateCallbackException;
import src.samples.method2.callback.exceptions.NoAnnotationException;

public interface Callback {
    /**
     * コールバックメソッドの型も固定できるようにした場合(2)．
     * コールバックメソッドと同じとこにコールバックメソッドの引数を定義するクラスを用意しておき，そのクラスを呼び出し側からコールバックに渡していく方法．
     * 
     * ※1：コールバックメソッドの引数を定義する内部クラスはpublic staticであるべし．
     * ※2：※1で定義する内部クラスは，インタフェースArgsUseClassInterfaceを実装しているべし．
     * ※3：※1で定義する内部クラスのプロパティとgetterはprivateであるべし(内包しているクラスからはアクセスできるので)．
     * ※4：コールバックメソッドの引数には，※1で定義した内部クラスを型にすべし．
     * ※5：コールバックを呼び出す側で引数を設定する際は，※1で定義する内部クラスのインスタンスを用いるべし．
     * 
     * @param methodName
     * @param args
     */
    public default void callback(String methodName, CallbackArgsInterface args) throws NoAnnotationException, CannotRunPrivateCallbackException {
        try {
            // ↓コールバックを呼び出している側で，Callbackインタフェースを実装したクラスでインスタンス化されている場合に，そのクラスのクラス名が取得されるはず
            // System.out.println(this.getClass());
            // System.out.println(Callback.class);
            // ↓コールバックを呼び出している側で，CallbackArgsInterfaceインタフェースを実装した内部クラスで引数を渡されている場合に，内部クラスのクラス名が取得されるはず
            // System.out.println(args.getClass());

            Class<?> callbackClass = Class.forName(this.getClass().getName());
            Object callbackInstance = callbackClass.newInstance();

            Method callbackMethod = callbackClass.getMethod(methodName, args.getClass());
            if (!callbackMethod.isAnnotationPresent(CallbackMethod.class)) {
                throw new NoAnnotationException("NoAnnotationException: Called method without annotation '@CallbackMethod'.");
            }
            callbackMethod.invoke(callbackInstance, args);
        } catch (NoAnnotationException e) {
            throw e;
        } catch (NoSuchMethodException e) {
            throw new CannotRunPrivateCallbackException("CannotRunPrivateCallbackException: Called private callback.");
        } catch(Exception e) { // Simple Exception
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}

