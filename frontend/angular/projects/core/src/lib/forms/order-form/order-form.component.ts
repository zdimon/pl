


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
  subCategoryId: number;
  categoryId: number;

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
    this.categoryId = event.value;
    this.subCategories = this.categoryStore.select(selectSubCategoriesByCategoryId(this.categoryId));
    this.api.getFormFields(this.categoryId).subscribe((rez: any) => {
      this.buildForm(rez.results);
    });
  }

  changeSubCategory(event) {
    this.subCategoryId = event.value;
    this.api.getFormFields(this.categoryId).subscribe((rez: any) => {
      this.buildForm(rez.results);
    });
  }

  buildForm(data: any) {
    console.log('Build form');
    console.log(data);
    this.controls = [];
    for (let field in data) {
      if (data.hasOwnProperty(field)) {
        //console.log(data[field].subcategory.includes(this.subCategoryId));
        if(this.subCategoryId) {
          if(data[field].subcategory.includes(this.subCategoryId)) {
            this.controls.push(data[field]);
            if (data[field].type === 'Checkbox') {
              this.form.addControl(data[field].alias, this.buildMany(data[field].option));
            } else {
              this.form.addControl(data[field].alias, new FormControl(''));
            }
          }
        } else {
          this.controls.push(data[field]);
          if (data[field].type === 'Checkbox') {
            this.form.addControl(data[field].alias, this.buildMany(data[field].option));
          } else {
            this.form.addControl(data[field].alias, new FormControl(''));
          }
        }
      }
    }
  }

  buildMany(options: any) {
    const arr = options.map(item => {
      return this.fb.control(false);
    });
    return this.fb.array(arr);
  }

  onSubmit(){
    
    const data = {
      title: this.form.get('title').value,
      desc: this.form.get('desc').value,
      category: this.form.get('category').value,
      subcategory: this.form.get('subCategory').value,
      controls: []
    };
    for (let cnrl of this.controls) {
      console.log(this.controls);
      let item = {};
      item['value'] = this.form.get(cnrl['alias']).value;
      item['control'] = cnrl.id;
      item['type'] = cnrl.type;
      //item[cnrl.alias] = this.form.get(cnrl['alias']).value;
      data.controls.push(item);
    }

    console.log(data);


    this.api.saveOrder(data).subscribe((res: any) => {
      console.log(res);
    });
  }


}
