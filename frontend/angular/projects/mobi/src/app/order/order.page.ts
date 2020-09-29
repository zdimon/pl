
import { Observable } from 'rxjs';
import { ApiService } from './../../../../core/src/lib/services/api.service';
import { Component } from '@angular/core';
import { PerfectScrollbarConfigInterface, PerfectScrollbarDirective } from 'ngx-perfect-scrollbar';


/// Store

import { Store } from '@ngrx/store';
import { OrderListState } from './../../../../core/src/lib/store/states/order.state';
import * as orderActions from './../../../../core/src/lib/store/actions/order.action';
import { selectOrderList } from './../../../../core/src/lib/store/selectors/order.selector';


@Component({
  selector: 'app-order',
  templateUrl: 'order.page.html',
  styleUrls: ['order.page.scss']
})
export class OrderPageComponent {
  public perfectScrollbarConfig: PerfectScrollbarConfigInterface = {};
  orders: Observable<any>;
  page = 1;
 

  constructor(
    private api: ApiService,
    private orderStore: Store<OrderListState>
    ) {
    this.api.getOrderList(this.page).subscribe((data: any) => {
        this.orderStore.dispatch(new orderActions.UpdateAllOrders(data.results));
    });
    this.orders = this.orderStore.select(selectOrderList);
  }


  onScrollDown(event){
    this.page += 1;
    
    console.log('Loading');
    this.api.getOrderList(this.page).subscribe((data: any) => {
      this.orderStore.dispatch(new orderActions.AddOrders(data.results));
      event.target.complete();
    });
  }

}
