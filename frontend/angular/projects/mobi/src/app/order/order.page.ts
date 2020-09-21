import { ApiService } from './../../../../core/src/lib/services/api.service';
import { Component } from '@angular/core';


@Component({
  selector: 'app-order',
  templateUrl: 'order.page.html',
  styleUrls: ['order.page.scss']
})
export class OrderPageComponent {

  orders: any;

  constructor(private api: ApiService) {
    this.api.getOrderList().subscribe((data: any) => {
        // console.log(data.results);
        this.orders = data.results;
    });
  }




}
