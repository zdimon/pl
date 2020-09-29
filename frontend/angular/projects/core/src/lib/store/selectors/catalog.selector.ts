import { createSelector, createFeatureSelector } from '@ngrx/store';
import { SubCategoryState, SubCategoryListState } from './../states/subcategory.state';
import { CategoryListState } from './../states/category.state';




export const getCategoryStateSelector = createFeatureSelector<CategoryListState>('category');

export const getSubCategoryStateSelector = createFeatureSelector<SubCategoryListState>('subcategory');

export const selectCategoryIds = createSelector(
    getCategoryStateSelector,
    (state: CategoryListState) => state.ids
);

export const selectCategoryEntities = createSelector(
    getCategoryStateSelector,
    (state: CategoryListState) => state.entities
);

export const selectSubCategoryEntities = createSelector(
    getSubCategoryStateSelector,
    (state: SubCategoryListState) => state.entities
);



export const selectCategory = createSelector(
    selectCategoryIds,
    selectCategoryEntities,
    selectSubCategoryEntities,
    (ids: any, cats: any, subs: any) => {
        return ids.map((el) => { 
                const cat = cats[el];
                cat.subcategory = [];
                for (let subid in subs) {
                    if (subs[subid].category === el) {
                        cat.subcategory.push(subs[subid]);
                    }
                }
                return cat;
            }
        )
    }
);
