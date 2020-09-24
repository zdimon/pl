import { NgModule } from '@angular/core';
import { CoreComponent } from './core.component';

import {MatInputModule} from '@angular/material';
import {MatCardModule} from '@angular/material/card';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatDatepickerModule} from '@angular/material/datepicker';
import { RegistrationFormComponent } from './forms/registration-form/registration-form.component';

import { ApiService } from './services/api.service';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import {ReactiveFormsModule} from '@angular/forms';

import { CommonModule } from '@angular/common';


@NgModule({
  declarations: [
    CoreComponent, 
    RegistrationFormComponent
  ],
  imports: [
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatButtonModule,
    MatSelectModule,
    MatDatepickerModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule,
    CommonModule
  ],
  providers: [
    ApiService
  ],
  exports: [CoreComponent, RegistrationFormComponent]
})
export class CoreModule { }
