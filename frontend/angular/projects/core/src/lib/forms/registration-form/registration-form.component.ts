import { ApiService } from './../../services/api.service';
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged } from 'rxjs/operators';



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
  error: string;


  constructor(private api: ApiService) { }

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
        console.log(res);
        if(res.status === 2) {
          this.error = res.message;
          this.status = 2;
        }
    });
  }

  doRegistration(){

  }

}
