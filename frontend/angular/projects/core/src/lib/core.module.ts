
import { NgModule } from '@angular/core';
import { CoreComponent } from './core.component';

import {MatInputModule} from '@angular/material';
import {MatCardModule} from '@angular/material/card';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatCheckboxModule} from '@angular/material/checkbox';


import { RegistrationFormComponent } from './forms/registration-form/registration-form.component';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import {ReactiveFormsModule} from '@angular/forms';

import { CommonModule } from '@angular/common';

import { FlexLayoutModule } from '@angular/flex-layout';
import { ProfileFormComponent } from './forms/profile-form/profile-form.component';


import { HTTP_INTERCEPTORS } from '@angular/common/http';

import { AuthInterceptor } from './interceptors/auth.interceptor';

export const interceptorProviders = [
  { 
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  }
];



import { InitService } from './services/init.service';
import { OrderFormComponent } from './forms/order-form/order-form.component';

export function init_app(initService: InitService) {
  return () => initService.init();
}



@NgModule({
  declarations: [
    CoreComponent, 
    RegistrationFormComponent, ProfileFormComponent, OrderFormComponent
  ],
  imports: [
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatButtonModule,
    MatSelectModule,
    MatDatepickerModule,
    MatCheckboxModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatCardModule,
    CommonModule,
    FlexLayoutModule
  ],
  providers: [
    interceptorProviders
  ],
  exports: [
    CoreComponent,
    RegistrationFormComponent,
    ProfileFormComponent,
    OrderFormComponent
  ]
})
export class CoreModule { }
