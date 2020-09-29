import { EntityState } from '@ngrx/entity';

export interface ICategorySatate {
    id: number;
    name: string;
}

export class CategoryState implements ICategorySatate {
    constructor(
        public id: number,
        public name: string) {
    }
}

export interface CategoryListState extends EntityState<CategoryState> {
}

export const defaultState = {};
