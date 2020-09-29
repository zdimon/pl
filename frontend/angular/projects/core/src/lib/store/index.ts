
import { ActionReducerMap } from '@ngrx/store';

import { SessionState } from './states/session.state';
import {SessionReducer} from './reducers/session.reducer';

import { CategoryListState } from './states/category.state';
import {CategoryReducer} from './reducers/category.reducer';

import { SubCategoryListState } from './states/subcategory.state';
import {SubCategoryReducer} from './reducers/subcategory.reducer';

export interface State {
    session: SessionState;
    category: CategoryListState;
    subcategory: SubCategoryListState;
}

export const reducers: ActionReducerMap<State> = {
    session: SessionReducer,
    category: CategoryReducer,
    subcategory: SubCategoryReducer
};