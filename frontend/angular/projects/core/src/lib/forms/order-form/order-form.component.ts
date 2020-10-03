


import { Observable } from 'rxjs';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators, FormControl } from '@angular/forms';

// Store
import { Store } from '@ngrx/store';
import { CategoryListState } from './../../store/states/category.state';
import { selectCategoryArray, selectSubCategoriesByCategoryId } from './../../store/selectors/catalog.selector';

// Services

import { ApiService } from './../../services/api.service';


@Component({
  selector: 'core-order-form',
  templateUrl: './order-form.component.html',
  styleUrls: ['./order-form.component.scss']
})
export class OrderFormComponent implements OnInit {

  form: any;
  categories: Observable<any>;
  subCategories: Observable<any>;
  controls: any;

  constructor(
    private fb: FormBuilder,
    private categoryStore: Store<CategoryListState>,
    private api: ApiService
    ) {
      this.categories = this.categoryStore.select(selectCategoryArray);
  }

  ngOnInit() {
    this.form = this.fb.group({
      title: ['', Validators.required],
      desc: [''],
      category: [''],
      subCategory: ['']
    });
  }

  changeCategory(event) {
    this.subCategories = this.categoryStore.select(selectSubCategoriesByCategoryId(event.value));
    this.api.getFormFields(event.value).subscribe((rez: any) => {
      this.buildForm(rez);
      this.controls = rez.results;
    });
  }

  changeSubCategory(event) {
    console.log(event.value);
  }

  buildForm(data: any) {
    console.log('Build form');
    console.log(data);
    for (let field in data.results) {
      if (data.results.hasOwnProperty(field)) {
        this.form.addControl(data.results[field].alias, new FormControl(''));
      }
    }
  }

}
