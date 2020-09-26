import { ApiService } from './../../services/api.service';
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';

import { SessionService } from './../../services/session.service';

@Component({
  selector: 'core-registration-form',
  templateUrl: './registration-form.component.html',
  styleUrls: ['./registration-form.component.scss']
})
export class RegistrationFormComponent implements OnInit {

  private loginControl: FormControl;
  login: string;
  password: string;
  status = 3;
  done = false;
  message: string;


  constructor(
    private api: ApiService,
    private session: SessionService) { }

  ngOnInit() {

    this.loginControl = new FormControl('');
    this.loginControl.valueChanges
    .pipe(debounceTime(1000))
    .subscribe(() => {
      const data = {email: this.loginControl.value}
      this.api.checkEmail(data).subscribe((res: any) => {
        this.status = res.status;
      });
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
          this.session.setIsAuth(true);
          this.session.setToken(res.token);
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

}
