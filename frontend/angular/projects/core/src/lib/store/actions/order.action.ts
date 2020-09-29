
import { Action } from '@ngrx/store';
import { CategoryState } from './../states/category.state';
import { OrderState } from './../states/order.state';

export enum OrderActionTypes {
    UpdateAllOrders = '[Order] update all orders',
    AddOrders = '[Order] add orders'
}

export class UpdateAllOrders implements Action {
    readonly type = OrderActionTypes.UpdateAllOrders;
    constructor(public payload: OrderState[]) {}
  }

export class AddOrders implements Action {
    readonly type = OrderActionTypes.AddOrders;
    constructor(public payload: OrderState[]) {}
  }

export type ActionsUnion = UpdateAllOrders | AddOrders;