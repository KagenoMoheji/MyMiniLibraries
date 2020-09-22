export interface CounterState {
  	count: number;
}

export interface CounterStateList {
	[key: string]: CounterState,
	counter1: CounterState,
	counter2: CounterState,
}