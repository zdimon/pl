import { EntityState } from '@ngrx/entity';

export interface IOrderSatate {
    id: number;
    title: string;
    desc: string;
}

export class OrderState implements IOrderSatate {
    constructor(
        public id: number,
        public title: string,
        public desc: string) {
    }
}

export interface OrderListState extends EntityState<OrderState> {
}

export const defaultState = {};
