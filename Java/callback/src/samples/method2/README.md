# Callback with arguments in Java
- Using interface and inner class.

### How to use
1. Copy `callback/`.
2. Create callback like below.
    ```
    import callback.*;
    import callback.annotations.CallbackMethod;
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
            return args.getArgStr() + ", " + args.getArgInt();
        }
    }
    ```
    - Rules
        - Import the following libraries.
            - `callback.*`
            - `callback.annotations.CallbackMethod`
        - Implement `Callback`(ex. `CallbackSample`).
        - Prepare type of arguments for callback method with Inner Class(ex. `ArgsForCallback`).
            - The modifier of Inner Class should be `public static`.
            - Inner Class should implement `CallbackArgsInterface`.
            - Add arguments, and implement public constructor and private getters.
        - Pepaere callback methods(ex. `callbackPrint()`, `callbackReturnString()`).
            - Add annotation `@CallbackMethod`.
            - Set the argument whose type is prepared with Inner Class.
3. Create caller like below.
    ```
    import callback.*;
    import callback.annotations.CallerMethod;
    import callback.exceptions.*;
    public class CallerSample {
        @CallerMethod
        public void callerSample(Callback callbackInstance, String methodName, CallbackArgsInterface args) {
            try {
                ...

                // If the type of callback is void
                callbackInstance.callback(methodName, args);
                // Or, if callback has return
                String ret = (String)callbackInstance.callbackHasReturn(methodName, args);

                ...
            } catch(NoAnnotationException | CannotRunPrivateCallbackException e) {
                System.out.println(e.getMessage());
                e.printStackTrace();
            }
        }
    }
    ```
    - Rules
        - Import the following libraries.
            - `callback.*`
            - `callback.annotations.CallerMethod`
            - `callback.exceptions.*`
        - Pepaere caller methods(ex. `callerSample()`).
            - Add annotation `@CallbackMethod`(It doesn't matter if you don't add now).
            - Set `Calllback callbackInterface`, `String methodName`, and `CallbackArgsInterface args` to the arguments of caller method.
            - Add try-catch to get exceptions `NoAnnotationException` or `CannotRunPrivateCallbackException`.
            - In try-catch, you can implement callback method.
                - Use `callback(methodName, args)` if callback method has no return(type void).
                - Use `callbackHasReturn(methodName, args)` if callback method has return.  
                However, you need type casting.
4. Let's run callback with code like below.
    ```
    public class Main {
        public static void main(String[] args) {
            CallerSample caller = new CallerSample();
            Callback callbackInstance = new CallbackSample();

            caller.callerSample(
                callerInstance,
                "callbackPrint",
                new ArgsForCallback("Height of Tokyo Skytree[m]: ", 634));

            caller.callerSample(
                callerInstance,
                "callbackReturnString",
                new ArgsForCallback("Height of Mt.Fuji[m]: ", 3776));
        }
    }
    ```
    - Rules
        - Make caller class materialize with class prepared at '3.'.
        - Make callback class materialize with class prepared at '2.'.  
        However, declare the type with interface `Callback`.
        - Run caller by setting arguments following.
            - `Callback callbackInstance`: Set materialized callback class.
            - `String methodName`: Set name of callback method.
            - `CallbackArgsInterface args`: Materialize inner class(type of arguments for callback method) prepared at '2.' and set arguments for callback mathod.
