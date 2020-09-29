import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/category.action';

import {CategoryState, CategoryListState, defaultState} from '../states/category.state';

export const adapter: EntityAdapter<CategoryState> = createEntityAdapter<CategoryState>();

export const initialState: CategoryListState = adapter.getInitialState(defaultState);

export function CategoryReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.CategoryActionTypes.UpdateCategories:
          return adapter.addAll(action.payload, state);

        default:
        return state;

    }
}