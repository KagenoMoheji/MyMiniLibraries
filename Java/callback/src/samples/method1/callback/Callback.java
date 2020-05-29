package src.samples.method1.callback;

import java.util.*;
import java.lang.reflect.*;

public interface Callback {
    /**
     *  コールバックメソッドの引数をHashMapで渡す場合．
     *  ※1：コールバックメソッド側で受け取る引数をHashMapにしておく必要があり，引数の
     *  　 　使用には「args.get("<引数名>")」のように記述しなければならない．
     *  -> callbackFixTypesで簡略化させる…と思ったが無理そう？？？
     *  ※2：引数の型判定をコールバックされるメソッド内で判定しなければならない．
     *  -> callbackFixTypesで引数の型も渡しておけるようにする．
     *  ※3：コールバックメソッドをObjectのサブであるIntegerやString等の型にしたとしても，コールバックメソッドに渡す引数の型をその1つに限定されてしまう．
     *  -> callbackFixTypesで異なる型の引数を渡せるようにする
     * @param methodName
     * @param args
     */
    public default void callback(String methodName, HashMap<String, Object> args) {
        try {
            Class<?> callbackClass = Class.forName(this.getClass().getName());
            Object callbackInstance = callbackClass.newInstance();
            
            Method callbackMethod = callbackClass.getMethod(methodName, HashMap.class);
            callbackMethod.invoke(callbackInstance, args);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}

