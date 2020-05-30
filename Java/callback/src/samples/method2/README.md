# Callback with arguments in Java
- Using interface and inner class.

### How to use
1. Copy `callback/`.
2. Create callback like below.
    ```
    import callback.*;
    public class CallbackSample implements Callback {
        public static ArgsForCallback implements CallbackArgsInterface {
            String argStr;
            int argInt;
            public ArgsForCallback(String argStr, int argInt) {
                this.argStr = argStr;
                this.argInt = argInt;
            }
            private getArgStr() {
                return this.argStr;
            }
            private getArgInt() {
                return this.argInt;
            }
        }

        @CallbackMethod
        public void callbackPrint(ArgsForCallback args) {
            System.out.println(args.getArgStr() + ", " + args.getArgInt());
        }

        @CallbackMethod
        public String callbackReturnString(ArgsForCallback args) {
            return args.getArgStr() + ", " + args.getArgInt()
        }
    }
    ```
    - Rules
        - Implement `Callback`(ex. `CallbackSample`).
        - Prepare type of arguments for callback method with Inner Class(ex. `ArgsForCallback`).
            - The modifier of Inner Class should be `public static`.
            - Inner Class should implement `CallbackArgsInterface`.
            - Add arguments, and implement public constructor and private getters.