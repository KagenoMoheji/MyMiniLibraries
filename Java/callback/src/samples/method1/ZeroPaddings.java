package src.samples.method1;

import java.util.*;
import src.samples.method1.callback.*;

public class ZeroPaddings implements Callback {
    /*
    コールバック関数にして好きなタイミングで実行させたいメソッドを集めたクラス．
    今回はゼロ埋めの速度比較コード(時間計測処理の間に実行させたい)．
    */
    // Callback Method
    public void zeroPadding1(HashMap<String, Integer> args) throws Exception { // Integer l, Integer n
        // ここで，引数の有無判定と引数の型判定を行わないといけない
        // あるいは，引数の型指定でObjectのところを特定の型に指定．そうすると全ての引数に置いて1種類の型しか受け付けなくなってしまう
        // 処理速度測る上ではこのコード邪魔
        if(!args.containsKey("l") || !args.containsKey("n")) {
            throw new Exception("NoArgumentError");
        }
        System.out.println(String.format("%0" + args.get("l") + "d", args.get("n")));
    }

    // Callback Method
    public void zeroPadding2(HashMap<String, Integer> args) throws Exception { // Integer l, Integer n
        // ここで，引数の有無判定と引数の型判定を行わないといけない
        // あるいは，引数の型指定でObjectのところを特定の型に指定．そうすると全ての引数に置いて1種類の型しか受け付けなくなってしまう
        // 処理速度測る上ではこのコード邪魔
        if(!args.containsKey("l") || !args.containsKey("n")) {
            throw new Exception("NoArgumentError");
        }
        int nLen = (int)Math.log10((double)args.get("n")) + 1;
        String preStr = (nLen >= args.get("l")) ? "" : repeatStr("0", args.get("l") - nLen);
        System.out.println(preStr + args.get("n"));
    }

    // Callback Method
    public void zeroPadding3(HashMap<String, Integer> args) throws Exception { // Integer l, Integer n
        // ここで，引数の有無判定と引数の型判定を行わないといけない
        // あるいは，引数の型指定でObjectのところを特定の型に指定．そうすると全ての引数に置いて1種類の型しか受け付けなくなってしまう
        // 処理速度測る上ではこのコード邪魔
        if(!args.containsKey("l") || !args.containsKey("n")) {
            throw new Exception("NoArgumentError");
        }
        int nLen = Integer.toString(args.get("n")).length();
        String preStr = (nLen >= args.get("l")) ? "" : repeatStr("0", args.get("l") - nLen);
        System.out.println(preStr + args.get("n"));
    }

    // Callback Method
    public void zeroPadding4(HashMap<String, Integer> args) throws Exception { // Integer l, Integer n
        // ここで，引数の有無判定と引数の型判定を行わないといけない
        // あるいは，引数の型指定でObjectのところを特定の型に指定．そうすると全ての引数に置いて1種類の型しか受け付けなくなってしまう
        // 処理速度測る上ではこのコード邪魔
        if(!args.containsKey("l") || !args.containsKey("n")) {
            throw new Exception("NoArgumentError");
        }
        int nLen = getNumLenWithDividing10(args.get("n"));
        String preStr = (nLen >= args.get("l")) ? "" : repeatStr("0", args.get("l") - nLen);
        System.out.println(preStr + args.get("n"));
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