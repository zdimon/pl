import { Injectable } from '@angular/core';

import {environment} from '../../environments/environment';

// Store
import { Store } from '@ngrx/store';
import { SessionState } from './../store/states/session.state';
import * as sessionActions from './../store/actions/session.action';

import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class InitService {

  constructor(
    private sessionStore: Store<SessionState>,
    private http: HttpClient
  ) { }

  init() {
    this.http.get(`${environment.backendUrl}v1/ij/init`).subscribe((data: any) => {
      this.sessionStore.dispatch(new sessionActions.Init(data));
    })
  }


}
