
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderPageComponent } from './order.page';
import { NewOrderComponent } from './new/new.component';

const routes: Routes = [
  {
    path: '',
    component: OrderPageComponent,
  },
  {
    path: 'new',
    component: NewOrderComponent,
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class Tab1PageRoutingModule {}
