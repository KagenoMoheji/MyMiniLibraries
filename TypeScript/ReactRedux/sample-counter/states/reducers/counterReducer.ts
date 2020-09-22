import { CounterState } from "#/types";
import {
    incrementAction,
    decrementAction,
    CounterActionReturn,
} from "#/states/actions";

const initialState: CounterState = {
    count: 0,
};

export const counterReducer = (
    state: CounterState = initialState,
    action: CounterActionReturn
): CounterState => {
    switch (action.type) {
        case incrementAction().type:
            return {
                ...state,
                count: increment(state.count),
            };
        case decrementAction().type:
            return {
                ...state,
                count: decrement(state.count),
            };
        default:
            return state;
    }
};

export const increment = (n: number): number => {
    return n + 1;
};
export const decrement = (n: number): number => {
    return n - 1;
};
