import React from "react";
import { connect } from "react-redux";
import { Dispatch, Action } from "redux";
import { CounterState } from "#/types";
import {
    incrementAction,
    decrementAction,
    CounterAction,
} from "#/states/actions";
import "#/scss/Counter.scss";

interface CounterProps {
    counter: CounterState;
    increment: CounterAction;
    decrement: CounterAction;
}
class Counter extends React.Component<CounterProps> {
    constructor(props: CounterProps) {
        super(props);
    }

    render(): JSX.Element {
        return (
            <div className="counter">
                <span>
                    <button
                        type="button"
                        onClick={() => this.props.decrement()}
                    >
                        ー
                    </button>
                </span>
                <span>{this.props.counter.count}</span>
                <span>
                    <button
                        type="button"
                        onClick={() => this.props.increment()}
                    >
                        ＋
                    </button>
                </span>
            </div>
        );
    }
}

const mapState2Props = (state: CounterProps) => ({
    counter: state.counter,
});
const mapDispatch2Props = (dispatch: Dispatch<Action<string>>) => ({
    increment: () => dispatch(incrementAction()),
    decrement: () => dispatch(decrementAction()),
});
export const ConnCounter = connect(mapState2Props, mapDispatch2Props)(Counter);
