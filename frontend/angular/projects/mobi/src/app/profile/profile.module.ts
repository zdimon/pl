
import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProfilePageComponent } from './profile.page';


import { ProfilePageRoutingModule } from './profile-routing.module';

import {CoreModule} from '../../../../core/src/lib/core.module';



@NgModule({

  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    CoreModule,
    RouterModule.forChild([{ path: '', component: ProfilePageComponent }]),
    ProfilePageRoutingModule,
  ],
  declarations: [
    ProfilePageComponent
  ]
})
export class ProfilePageModule {}
