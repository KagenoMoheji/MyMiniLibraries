export interface CounterActionReturn {
    type: string;
    // payload: {};
}
export type CounterAction = () => CounterActionReturn;

export const incrementAction: CounterAction = () => ({
    type: "INC",
});
export const decrementAction: CounterAction = () => ({
    type: "DEC",
});
