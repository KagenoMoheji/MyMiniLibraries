import { combineReducers } from "redux";

import { counterReducer } from "#/states/reducers/counterReducer";

export const allReducers = combineReducers({
    counterList: counterReducer,
});
