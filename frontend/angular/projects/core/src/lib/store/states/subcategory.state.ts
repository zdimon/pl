import { EntityState } from '@ngrx/entity';

export interface ISubCategorySatate {
    id: number;
    name: string;
}

export class SubCategoryState implements ISubCategorySatate {
    constructor(
        public id: number,
        public name: string) {
    }
}

export interface SubCategoryListState extends EntityState<SubCategoryState> {
}

export const defaultState = {};
