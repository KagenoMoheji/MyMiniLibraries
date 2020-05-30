package src.research.callback;

// public class CallbackArg {
//     private final Class<?> TYPE;
//     private final Object VAL;
//     public CallbackArg(Class<?> type, Object val) {
//         this.TYPE = type;
//         this.VAL = val;
//     }

//     public Object getVAL() {
//         return this.VAL;
//     }
//     public Class<?> getTYPE() {
//         return this.TYPE;
//     }
// }

public class CallbackArg<T> { // implements CallbackArgInterface
    private Class<?> type;
    private T val;
    public CallbackArg(Class<?> type, T val) {
        try {
            if(!(val.getClass().getName().equals(type.getName()))) {
                throw new Exception("Exception: Type not match between arguments 'type' and 'val.'");
            }
            this.type = type;
            this.val = val;
        } catch(Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    public T getVal() {
        return this.val;
    }
    public Class<?> getType() {
        return this.type;
    }
}