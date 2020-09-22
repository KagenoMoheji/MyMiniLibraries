import React from "react";
import { connect } from "react-redux";
import { Dispatch, Action } from "redux";
import { CounterStateList } from "#/types";
import {
    incrementAction,
    decrementAction,
    CounterAction,
} from "#/states/actions";
import "#/scss/Counter.scss";

interface CounterProps {
    counterId: string;
    counterList: CounterStateList;
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
                        onClick={() =>
                            this.props.decrement(this.props.counterId)
                        }
                    >
                        ー
                    </button>
                </span>
                <span>
                    {this.props.counterList[this.props.counterId].count}
                </span>
                <span>
                    <button
                        type="button"
                        onClick={() =>
                            this.props.increment(this.props.counterId)
                        }
                    >
                        ＋
                    </button>
                </span>
            </div>
        );
    }
}

const mapState2Props = (state: CounterProps) => ({
    counterList: state.counterList,
});
const mapDispatch2Props = (dispatch: Dispatch<Action<string>>) => ({
    increment: (counterId?: string) => dispatch(incrementAction(counterId)),
    decrement: (counterId?: string) => dispatch(decrementAction(counterId)),
});
export const ConnCounter = connect(mapState2Props, mapDispatch2Props)(Counter);
