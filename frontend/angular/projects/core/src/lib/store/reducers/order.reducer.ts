import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/order.action';

import {OrderState, OrderListState, defaultState} from '../states/order.state';

export const adapter: EntityAdapter<OrderState> = createEntityAdapter<OrderState>();

export const initialState: OrderListState = adapter.getInitialState(defaultState);

export function OrderReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.OrderActionTypes.UpdateAllOrders:
          return adapter.addAll(action.payload, state);

        case Actions.OrderActionTypes.AddOrders:
          return adapter.addMany(action.payload, state);

        default:
          return state;

    }
}