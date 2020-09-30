

import { Observable } from 'rxjs';
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';

// Store
import { Store } from '@ngrx/store';
import { CategoryListState } from './../../store/states/category.state';
import { selectCategoryArray, selectSubCategoriesByCategoryId } from './../../store/selectors/catalog.selector';


@Component({
  selector: 'core-order-form',
  templateUrl: './order-form.component.html',
  styleUrls: ['./order-form.component.scss']
})
export class OrderFormComponent implements OnInit {

  form: any;
  categories: Observable<any>;
  subCategories: Observable<any>;

  constructor(
    private fb: FormBuilder,
    private categoryStore: Store<CategoryListState>
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
  }

  changeSubCategory(event) {
    console.log(event.value);
  }

}
