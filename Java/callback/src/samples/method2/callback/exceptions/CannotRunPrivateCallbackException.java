package src.samples.method2.callback.exceptions;

public class CannotRunPrivateCallbackException extends Exception {
    public CannotRunPrivateCallbackException(String msg) {
        super(msg);
    }
}