export interface CounterActionReturn {
    type: string;
    payload: {
        counterId?: string;
    };
}
export type CounterAction = (counterId?: string) => CounterActionReturn;

export const incrementAction: CounterAction = (counterId?) => ({
    type: "INC",
    payload: {
        counterId: counterId,
    },
});
export const decrementAction: CounterAction = (counterId?) => ({
    type: "DEC",
    payload: {
        counterId: counterId,
    },
});
