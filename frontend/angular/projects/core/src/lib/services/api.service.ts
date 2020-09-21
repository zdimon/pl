import { Injectable } from '@angular/core';
import {environment} from '../../environments/environment';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }


  test(){
    alert(environment.backendUrl);
  }


  getOrderList(){
    return this.http.get(`${environment.backendUrl}v1/ij/order/list`);
  }

  getCategoryList(){
    return this.http.get(`${environment.backendUrl}v1/ij/category/list`);
  }


}
