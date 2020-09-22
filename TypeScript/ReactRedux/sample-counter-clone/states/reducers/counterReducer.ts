import { CounterStateList } from "#/types";
import {
    incrementAction,
    decrementAction,
    CounterActionReturn,
} from "#/states/actions";

const initialState: CounterStateList = {
    counter1: {
        count: 0,
    },
    counter2: {
        count: 0,
    },
};

export const counterReducer = (
    state: CounterStateList = initialState,
    action: CounterActionReturn
): CounterStateList => {
    switch (action.type) {
        case incrementAction().type:
            return {
                ...state,
                [action.payload.counterId!]: {
                    count: increment(state[action.payload.counterId!].count), // (*)イベント起きた後，つまりレンダリング終了後の処理なので，どのみちcounterIdは存在するはず
                },
            };
        case decrementAction().type:
            return {
                ...state,
                [action.payload.counterId!]: {
                    count: decrement(state[action.payload.counterId!].count), // (*)イベント起きた後，つまりレンダリング終了後の処理なので，どのみちcounterIdは存在するはず
                },
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
