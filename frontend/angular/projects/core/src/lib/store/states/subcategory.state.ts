import { EntityState } from '@ngrx/entity';

export interface ISubCategorySatate {
    id: number;
    name: string;
    is_filtered: boolean;
}

export class SubCategoryState implements ISubCategorySatate {
    constructor(
        public id: number,
        public name: string,
        public is_filtered: boolean) {
    }
}

export interface SubCategoryListState extends EntityState<SubCategoryState> {
}

export const defaultState = {};
