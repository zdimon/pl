import { ApiService } from './../../services/api.service';
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';

import { SessionService } from './../../services/session.service';

import { Store } from '@ngrx/store';
import * as sessionActions from '../../store/actions/session.action';
import { SessionState } from '../../store/states/session.state';

import { AuthService } from "angularx-social-login";
import { GoogleLoginProvider } from "angularx-social-login";

@Component({
  selector: 'core-registration-form',
  templateUrl: './registration-form.component.html',
  styleUrls: ['./registration-form.component.scss']
})
export class RegistrationFormComponent implements OnInit {

  private loginControl: FormControl;
  login = '';
  password: string;
  status = 3;
  done = false;
  message: string;


  constructor(
    private api: ApiService,
    private session: SessionService,
    private sessionStore: Store<SessionState>,
    private authService: AuthService
    ) { }

  ngOnInit() {

    this.loginControl = new FormControl('');
    this.loginControl.valueChanges
    .pipe(debounceTime(1000))
    .subscribe(() => {
      if(this.login.length > 2) {
        const data = {email: this.loginControl.value}
        this.api.checkEmail(data).subscribe((res: any) => {
          this.status = res.status;
        });
      }
    });

  }

  doLogin(){
    const data = {
      username: this.login,
      password: this.password
    };
    this.api.login(data).subscribe((res: any) => {
        if(res.status === 2) {
          this.message = res.message;
          this.status = 2;
        } else {
          this.session.login(res);
        }
    });
  }

  doRegistration(){
    const data = {
      email: this.login
    };
    this.api.registration(data).subscribe((res) => {
      this.status = 2;
      this.message = 'Спасибо, вы были зарегистрированы и пароль был отправлен на emeil.'
    });
  }

  doLoginByGoogle(){
    console.log('reg by google');
    this.authService.signIn(GoogleLoginProvider.PROVIDER_ID).then((data: any) => {
     
      this.authService.authState.subscribe(user => {
        console.log(user);
        this.api.loginByGoogle(user).subscribe((rez) => {
          console.log(rez);
          this.session.login(rez);
        });
        
      });
    });
  }

}
