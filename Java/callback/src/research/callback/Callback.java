package src.research.callback;

import java.util.*;
import java.util.Map.Entry;
import java.lang.reflect.*;

public interface Callback {
    // ★サブクラスでオーバーライド
    // public void callbackOverride(String methodName, HashMap<String, Object> args);

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
    public default void callbackWithHashmap(String methodName, HashMap<String, Object> args) {
        try {
            Class<?> callbackClass = Class.forName(this.getClass().getName());
            Object callbackInstance = callbackClass.newInstance();
            
            Method callbackMethod = callbackClass.getMethod(methodName, HashMap.class);
            callbackMethod.invoke(callbackInstance, args);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    /**
     *  コールバックメソッドの型も固定できるようにした場合(1)．
     *  変数名をキーに，ジェネリック型の引数オブジェクト(型と値)CallbackArgをバリューとするHashMapを用いる方法．
     *  うまくいっていない．
     * 
     *  コールバックメソッドを呼び出す側で渡す引数には，
     *  ```
     *  // 注意！：HashMapについては下記は簡易記述．基本的に別途宣言して変数を第2引数に入れるべき．
     *  callback("<メソッド名>", new HashMap<String, Object>(){
     *      put("n", new CallbackArg<Integer>(10));
     *      put("s", new CallbackArg<String>("str"));
     *  });
     *  ```
     * @param methodName
     * @param args
     */
    public default void callbackFixTypes(String methodName, HashMap<String, Object> args) {
        try {
            for(Entry<String, Object> entry: args.entrySet()) {
                System.out.println(entry.getValue());
                System.out.println(entry.getValue().getClass().getName());
                // System.out.println(entry.getValue().getTYPE());
            }
            // Class<?> callbackClass = Class.forName(this.getClass().getName());
            // Object callbackInstance = callbackClass.newInstance();
            
            // Method callbackMethod = callbackClass.getMethod(methodName, HashMap.class);
            // callbackMethod.invoke(callbackInstance, args);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    /**
     *  コールバックメソッドの型も固定できるようにした場合(2)．
     *  コールバックメソッドと同じとこにコールバックメソッドの引数を定義するクラスを用意しておき，そのクラスを呼び出し側からコールバックに渡していく方法．
     * 
     *  ※1：コールバックメソッドの引数を定義する内部クラスはpublic staticであるべし．
     *  ※2：※1で定義する内部クラスは，インタフェースArgsUseClassInterfaceを実装しているべし．
     *  ※3：コールバックを呼び出す側で引数を設定する際は，※1で定義する内部クラスのインスタンスを用いるべし．
     *  
     * @param methodName
     * @param args
     */
    public default void callbackUseClass(String methodName, ArgsUseClassInterface args) {
        try {
            Class<?> callbackClass = Class.forName(this.getClass().getName());
            Object callbackInstance = callbackClass.newInstance();
            // System.out.println(args.getClass());
            
            Method callbackMethod = callbackClass.getMethod(methodName, args.getClass());
            callbackMethod.invoke(callbackInstance, args);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}


// 【Java入門】リフレクションでメソッドの実行、フィールドの変更
// https://www.sejuku.net/blog/33252

// リフレクション
// https://www.ne.jp/asahi/hishidama/home/tech/java/reflection.html

// [Java] クラスからクラス名を取得する
// https://blog.java-reference.com/java-class-getname/

// Getting the name of a sub-class from within a super-class(スーパークラス内からサブクラスの名前を取得する)
// https://stackoverflow.com/questions/3417879/getting-the-name-of-a-sub-class-from-within-a-super-class

// インターフェースのデフォルトメソッド
// http://www.ne.jp/asahi/hishidama/home/tech/java/interface.html#h_default_method

// 【Java入門】Map(HashMap)の宣言と初期化をする方法(定数化も解説)
// https://www.sejuku.net/blog/15842

// unreported exception ClassNotFoundException;must be caught or declared to be thrown
// https://stackoverflow.com/questions/28673740/unreported-exception-classnotfoundexceptionmust-be-caught-or-declared-to-be-thr?rq=1

// Getting the name of a sub-class from within a super-class
// https://stackoverflow.com/a/3417967

// How do I pass a class as a parameter in Java?
// https://stackoverflow.com/a/25055557

// Can I pass an array as arguments to a method with variable arguments in Java?
// https://stackoverflow.com/a/2926653

// EntrySetが便利な件 (HashMapをforするときはEntrySet>keySetである)
// https://qiita.com/RO018/items/e756089312bbd6c353a9

// Get generic type of class at runtime
// https://stackoverflow.com/a/3403987

// How to Use the instanceof Operator with a Generic Class in Java
// https://www.webucator.com/how-to/how-use-the-instanceof-operator-with-generic-class-java.cfm

// No enclosing instance of type Hoge is accessible.
// https://qiita.com/watanabk/items/738988fac29e1e1d8d88#fuga-%E3%82%92-static-%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AB%E3%81%99%E3%82%8B

// javaの内部クラスおさらい
// https://qiita.com/liguofeng29/items/6cafca5bf92e0381ee42#static%E5%86%85%E9%83%A8%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AE%E7%89%B9%E5%BE%B4

// リフレクションでフィールドのアノテーションの有無を調べる
// https://java-beginner.com/reflect-field-annotation-present/