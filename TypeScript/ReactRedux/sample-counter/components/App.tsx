import React from "react";
import { ConnCounter } from "#/components/counter/Counter";

export class App extends React.Component {
    render(): JSX.Element {
        return (
            <div>
                <ConnCounter />
            </div>
        );
    }
}
