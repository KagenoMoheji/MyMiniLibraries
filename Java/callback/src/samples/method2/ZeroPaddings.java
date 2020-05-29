package src.samples.method2;

import src.samples.method2.callback.*;

public class ZeroPaddings implements Callback {
    /*
    コールバック関数にして好きなタイミングで実行させたいメソッドを集めたクラス．
    今回はゼロ埋めの速度比較コード(時間計測処理の間に実行させたい)．
    */
    public static class ArgsZeroPaddingUseClass implements CallbackArgsInterface {
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

    public void zeroPadding1(ArgsZeroPaddingUseClass args) {
        System.out.println(String.format("%0" + args.getL() + "d", args.getN()));
    }

    public void zeroPadding2(ArgsZeroPaddingUseClass args) {
        int nLen = (int)Math.log10((double)args.getN()) + 1;
        String preStr = (nLen >= args.getL()) ? "" : repeatStr("0", args.getL() - nLen);
        System.out.println(preStr + args.getN());
    }

    public void zeroPadding3(ArgsZeroPaddingUseClass args) {
        int nLen = Integer.toString(args.getN()).length();
        String preStr = (nLen >= args.getL()) ? "" : repeatStr("0", args.getL() - nLen);
        System.out.println(preStr + args.getN());
    }

    public void zeroPadding4(ArgsZeroPaddingUseClass args) {
        int nLen = getNumLenWithDividing10(args.getN());
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

    public static int getNumLenWithDividing10(int n) {
        int nLen = 0;
        while(n != 0) {
            n /= 10;
            nLen++;
        }
        return nLen;
    }
}