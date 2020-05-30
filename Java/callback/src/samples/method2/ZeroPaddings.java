package src.samples.method2;

import src.samples.method2.callback.*;
import src.samples.method2.callback.annotations.CallbackMethod;

public class ZeroPaddings implements Callback {
    /*
    コールバック関数にして好きなタイミングで実行させたいメソッドを集めたクラス．
    今回はゼロ埋めの速度比較コード(時間計測処理の間に実行させたい)．
    */
    // Common argumens of callback methods
    public static class ArgsZeroPadding implements CallbackArgsInterface {
        private int l;
        private int n;
        ArgsZeroPadding(int l, int n) {
            this.l = l;
            this.n = n;
        }
        private int getL() {
            /**
             * 内部クラスのprivateメソッドは包括クラスで使えるが，外部クラスからはアクセスできない
             */
            return this.l;
        }
        private int getN() {
            return this.n;
        }
    }

    @CallbackMethod
    public void zeroPadding1(ArgsZeroPadding args) {
        System.out.println(String.format("%0" + args.getL() + "d", args.getN()));
    }

    @CallbackMethod
    public void zeroPadding2(ArgsZeroPadding args) {
        int nLen = (int)Math.log10((double)args.getN()) + 1;
        String preStr = (nLen >= args.getL()) ? "" : repeatStr("0", args.getL() - nLen);
        System.out.println(preStr + args.getN());
    }

    @CallbackMethod
    public void zeroPadding3(ArgsZeroPadding args) {
        int nLen = Integer.toString(args.getN()).length();
        String preStr = (nLen >= args.getL()) ? "" : repeatStr("0", args.getL() - nLen);
        System.out.println(preStr + args.getN());
    }

    @CallbackMethod
    public void zeroPadding4(ArgsZeroPadding args) {
        int nLen = getNumLenWithDividing10(args.getN());
        String preStr = (nLen >= args.getL()) ? "" : repeatStr("0", args.getL() - nLen);
        System.out.println(preStr + args.getN());
    }

    private String repeatStr(String str, int repeatNum) {
        String res = "";
        if(repeatNum == 0) {
            return res;
        }
        for(int i = 0; i < repeatNum; i++) {
            res += str;
        }
        return res;
    }

    private int getNumLenWithDividing10(int n) {
        int nLen = 0;
        while(n != 0) {
            n /= 10;
            nLen++;
        }
        return nLen;
    }


    public static class ArgsTestCannotBeCalled implements CallbackArgsInterface {
        int a;
        int b;
        ArgsTestCannotBeCalled(int a, int b) {
            this.a = a;
            this.b = b;
        }
        private int getA() {
            return this.a;
        }
        private int getB() {
            return this.b;
        }
    }
    public void testCannotBeCalledPublicWithoutAnnotation(ArgsTestCannotBeCalled args) {
        System.out.println(args.getA() + args.getB());
    }
    @CallbackMethod
    private int testCannotBeCalledPrivate(ArgsTestCannotBeCalled args) { // public
        return args.getA() + args.getB();
    }
}