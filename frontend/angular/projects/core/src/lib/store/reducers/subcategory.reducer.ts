import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/subcategory.action';

import {SubCategoryState, SubCategoryListState, defaultState} from '../states/subcategory.state';

export const adapter: EntityAdapter<SubCategoryState> = createEntityAdapter<SubCategoryState>();

export const initialState: SubCategoryListState = adapter.getInitialState(defaultState);

export function SubCategoryReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.SubCategoryActionTypes.UpdateSubCategories:
          return adapter.addAll(action.payload, state);

        default:
        return state;

    }
}