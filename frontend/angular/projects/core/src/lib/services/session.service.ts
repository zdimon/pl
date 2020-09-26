import { Injectable } from '@angular/core';

import { Store } from '@ngrx/store';
import * as sessionActions from '../store/actions/session.action';
import { SessionState } from '../store/states/session.state';

@Injectable({
  providedIn: 'root'
})
export class SessionService {
  storage: any;

  constructor(
    private sessionStore: Store<SessionState>
  ) { 
    this.storage = sessionStorage;
  }

  getToken(): string {
      return this.storage.getItem('access_token');
  }

  setToken(value: string) {
      this.storage.setItem('access_token', value);
  }

  removeToken() {
      this.storage.removeItem('access_token');
  }

  getIsAuth(): boolean {
      return this.storage.getItem('isAuth');
  }

  setIsAuth(value: boolean) {
      this.storage.setItem('isAuth', value);
  }

  login(data: any){
    this.sessionStore.dispatch(new sessionActions.LogIn(data));
  }

  logout(){
    this.removeToken();
    this.setIsAuth(false);
    this.sessionStore.dispatch(new sessionActions.LogOut());
  }

}
