package src.callback;

/**
 * コールする側は引数のargTypesに，例えば[String.class, Integer.class]という感じに書く
 */
public class ArgTuple {
    // public String name;
    private Class<?> argType;
    // private Object val;

    public ArgTuple(Class<?> argType, Object val) {
        this.argType = argType;
        // this.val = val;
    }

    public Class<?> getArgType() {
        return this.argType;
    }
    // public argType getVal() {
    //     return (argType)this.val;
    // }
}


