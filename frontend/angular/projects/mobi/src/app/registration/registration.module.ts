
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RegistrationComponent } from './registration.component';

import { RegistrationPageRoutingModule } from './registration-routing.module';

import { IonicModule } from '@ionic/angular';
import { FormsModule } from '@angular/forms';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';
import {CoreModule} from '../../../../core/src/lib/core.module';



@NgModule({
  declarations: [
    RegistrationComponent
  ],
  imports: [
    CommonModule,
    RegistrationPageRoutingModule,
    IonicModule,
    FormsModule,
    ExploreContainerComponentModule,
    CoreModule
  ]
})
export class RegistrationModule { }
