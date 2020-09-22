import { createStore } from "redux";

import { allReducers } from "#/states/reducers";

export const allStores = createStore(allReducers);
