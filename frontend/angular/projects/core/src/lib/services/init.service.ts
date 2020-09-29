import { reducers } from './../store/index';
import { Injectable } from '@angular/core';
import {scan} from 'rxjs/operators';
import {environment} from '../../environments/environment';

// Store
import { Store } from '@ngrx/store';
import { SessionState } from './../store/states/session.state';
import * as sessionActions from './../store/actions/session.action';

import { CategoryListState } from './../store/states/category.state';
import * as categoryActions from './../store/actions/category.action';

import { SubCategoryListState } from './../store/states/subcategory.state';
import * as subcategoryActions from './../store/actions/subcategory.action';

//////

import { ApiService } from './api.service';

import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class InitService {

  constructor(
    private sessionStore: Store<SessionState>,
    private categoryStore: Store<CategoryListState>,
    private subcategoryStore: Store<SubCategoryListState>,
    private http: HttpClient,
    private api: ApiService
  ) { }

  init() {
    this.http.get(`${environment.backendUrl}v1/ij/init`).subscribe((data: any) => {
      this.sessionStore.dispatch(new sessionActions.Init(data));
    });

    this.api.getCategoryList()
    .subscribe((data: any) => {
      const arrCat = data.map((el: any) => {
        return {id: el.id, name: el.name};
      });
      this.categoryStore.dispatch(new categoryActions.UpdateCategories(arrCat));

      const subcat = [];
      data.forEach(el => {
        subcat.push(el.subcategory);
      });
      //console.log(subcat.reduce((acc, val) => acc.concat(val), []));
      this.subcategoryStore.dispatch(new subcategoryActions.UpdateSubCategories(subcat.reduce((acc, val) => acc.concat(val), [])));
    });

  }


}
