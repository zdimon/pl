import { Action } from '@ngrx/store';
import { SubCategoryState } from '../states/subcategory.state';

export enum SubCategoryActionTypes {
    UpdateSubCategories = '[SubCategory] update categories'
}

export class UpdateSubCategories implements Action {
    readonly type = SubCategoryActionTypes.UpdateSubCategories;
    constructor(public payload: SubCategoryState[]) {}
  }

export type ActionsUnion = UpdateSubCategories;
