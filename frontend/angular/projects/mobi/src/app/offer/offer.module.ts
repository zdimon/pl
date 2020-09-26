import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { OfferPageComponent } from './offer.page';
import { ExploreContainerComponentModule } from '../explore-container/explore-container.module';
import {CoreModule} from '../../../../core/src/lib/core.module';
import { OfferPageRoutingModule } from './offer-routing.module';


@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    ExploreContainerComponentModule,
    OfferPageRoutingModule,
    CoreModule
  ],
  declarations: [OfferPageComponent]
})
export class OfferPageModule {}
