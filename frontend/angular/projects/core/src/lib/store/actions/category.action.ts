import { Action } from '@ngrx/store';
import { CategoryState } from './../states/category.state';

export enum CategoryActionTypes {
    UpdateCategories = '[Category] update categories'
}

export class UpdateCategories implements Action {
    readonly type = CategoryActionTypes.UpdateCategories;
    constructor(public payload: CategoryState[]) {}
  }

export type ActionsUnion = UpdateCategories;