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

  checkEmail(data: any){
    return this.http.post(`${environment.backendUrl}v1/ij/registration/check/email`,data);
  }

  login(data: any){
    return this.http.post(`${environment.backendUrl}v1/ij/login`,data);
  }

  registration(data: any){
    return this.http.post(`${environment.backendUrl}v1/ij/registration`,data);
  }

  loginByGoogle(data){
    return this.http.post(`${environment.backendUrl}v1/ij/google/auth`,data);
  }

  saveProfile(data,userId){
    return this.http.patch(`${environment.backendUrl}v1/ij/profile/edit/${userId}`, data);
  }


}
