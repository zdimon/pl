
import { createSelector, createFeatureSelector } from '@ngrx/store';
import { SubCategoryState, SubCategoryListState } from './../states/subcategory.state';
import { CategoryListState } from './../states/category.state';

import { selectUserFilter } from './session.selector';


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

export const selectCategoryArray = createSelector(
    selectCategoryIds,
    selectCategoryEntities,
    (ids: any, objs: any) => ids.map( id => objs[id] )
);

export const selectSubCategoryEntities = createSelector(
    getSubCategoryStateSelector,
    (state: SubCategoryListState) => state.entities
);

// TODO попробовать на reduce
export const selectSubCategoriesByCategoryId = (id: number) => {
    return createSelector(
        selectSubCategoryEntities,
        (objs: any) => {
            const out = [];
            for( let ido in objs) {
                if (objs[ido].category === id) out.push(objs[ido]);
            }
            return out;
        }
    );
}

export const selectCategory = createSelector(
    selectCategoryIds,
    selectCategoryEntities,
    selectSubCategoryEntities,
    selectUserFilter,
    (ids: any, cats: any, subs: any, userFilter: number[]) => {
        return ids.map((el) => { 
                const cat = cats[el];
                cat.subcategory = [];
                for (let subid in subs) {
                    let subcat = subs[subid];
                    if (userFilter.includes(parseInt(subid))) {
                        subcat.is_filtered = true;
                    } else {
                        subcat.is_filtered = false;
                    }
                    if (subs[subid].category === el) {
                        cat.subcategory.push(subcat);
                    }
                }
                return cat;
            }
        )
    }
);
