package src.research;

import java.util.*;
import src.research.callback.*;

public class ZeroPaddings implements Callback {
    /*
    コールバック関数にして好きなタイミングで実行させたいメソッドを集めたクラス．
    今回はゼロ埋めの比較コード．
    */
    public void zeroPadding1_WithHashmap(HashMap<String, Integer> args) { // int l, int n
        if(!args.containsKey("l") || !args.containsKey("n")) {
            return;
        }
        
        System.out.println(String.format("%0" + args.get("l") + "d", args.get("n")));
    }
    public void zeroPadding2_WithHashmap(HashMap<String, Integer> args) { // int l, int n
        if(!args.containsKey("l") || !args.containsKey("n")) {
            return;
        }
        
        int nLen = (int)Math.log10((double)args.get("n")) + 1;
        String preStr = (nLen >= args.get("l")) ? "" : repeatStr("0", args.get("l") - nLen);
        System.out.println(preStr + args.get("n"));
    }

    // public void zeroPadding1_FixTypes(int l, int n) {
    //     System.out.println(String.format("%0" + l + "d", n));
    // }
    // public void zeroPadding2_FixTypes(int l, int n) {
    //     int nLen = (int)Math.log10((double)n) + 1;
    //     String preStr = (nLen >= l) ? "" : repeatStr("0", l - nLen);
    //     System.out.println(preStr + n);
    // }

    public static class ArgsZeroPaddingUseClass implements ArgsUseClassInterface {
        private int l;
        private int n;
        ArgsZeroPaddingUseClass(int l, int n) {
            this.l = l;
            this.n = n;
        }
        public int getL() {
            return this.l;
        }
        public int getN() {
            return this.n;
        }
    }
    public void zeroPadding1_UseClass(ArgsZeroPaddingUseClass args) {
        System.out.println(String.format("%0" + args.getL() + "d", args.getN()));
    }
    public void zeroPadding2_UseClass(ArgsZeroPaddingUseClass args) {
        int nLen = (int)Math.log10((double)args.getN()) + 1;
        String preStr = (nLen >= args.getL()) ? "" : repeatStr("0", args.getL() - nLen);
        System.out.println(preStr + args.getN());
    }

    public String repeatStr(String str, int repeatNum) {
        String res = "";
        if(repeatNum == 0) {
            return res;
        }
        for(int i = 0; i < repeatNum; i++) {
            res += str;
        }
        return res;
    }

    public void test_WithHashmap(HashMap<String, Object> args) {
        System.out.println(args.get("n"));
        System.out.println(args.get("n").getClass());
        System.out.println(args.get("s"));
        System.out.println(args.get("s").getClass());
    }
    public void test2_WithHashmap(HashMap<String, Integer> args) {
        System.out.println(args.get("n"));
        System.out.println(args.get("n").getClass());
        System.out.println(args.get("s")); // エラー？
        System.out.println(args.get("s").getClass()); // エラー？
    }
    // public void test_FixTypes(HashMap<String, Object> args) {
    //     System.out.println(((CallbackArg)args.get("n")).getVAL());
    //     System.out.println(((CallbackArg)args.get("n")).getTYPE());
    //     System.out.println(((CallbackArg)args.get("s")).getVAL());
    //     System.out.println(((CallbackArg)args.get("s")).getTYPE());
    // }
    public static class ArgsTestUseClass {
        private int n;
        private String s;
        ArgsTestUseClass(int n, String s) {
            this.n = n;
            this.s = s;
        }
        public int getN() {
            return this.n;
        }
        public String getS() {
            return this.s;
        }
    }
    public void test_UseClass(ArgsTestUseClass args) {
        System.out.println(args.getN());
        System.out.println(args.getS());
    }
    
    // ★オーバーライド
    // public void callbackOverride(String methodName, HashMap<String, Object> args) {
    //     try {
    //         // (1-1)
    //         Class<?> callbackClass = Class.forName(this.getClass().getName()); // "ZeroPaddings"
    //         Object callbackInstance = callbackClass.newInstance();
    //         // (1-2)
    //         // Class<ZeroPaddings> callbackClass = ZeroPaddings.class;
    //         // Object callbackInstance = callbackClass.newInstance();
            
    //         Method callbackMethod = callbackClass.getMethod(methodName, HashMap.class);
    //         callbackMethod.invoke(callbackInstance, args);
    //     } catch(Exception e) {
    //         e.printStackTrace();
    //     }
    // }
}