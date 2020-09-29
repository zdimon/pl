
import { isDataSource } from '@angular/cdk/collections';
import { createSelector, createFeatureSelector } from '@ngrx/store';
import { OrderState, OrderListState } from './../states/order.state';


export const getOrderStateSelector = createFeatureSelector<OrderListState>('order');

export const selectOrderyIds = createSelector(
    getOrderStateSelector,
    (state: OrderListState) => state.ids
);

export const selectOrderEntities = createSelector(
    getOrderStateSelector,
    (state: OrderListState) => state.entities
);

export const selectOrderList = createSelector(
    selectOrderyIds,
    selectOrderEntities,
    (ids: any, objects: any) => ids.map( id => objects[id] )
);

