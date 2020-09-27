

import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

// Store
import { Store } from '@ngrx/store';
import { SessionState } from './../../store/states/session.state';
import { selectSessionUser } from './../../store/selectors/session.selector';
import * as sessionActions from './../../store/actions/session.action';

import { ApiService } from './../../services/api.service';

@Component({
  selector: 'core-profile-form',
  templateUrl: './profile-form.component.html',
  styleUrls: ['./profile-form.component.scss']
})
export class ProfileFormComponent implements OnInit {

  profileForm: any;
  user: any;

  constructor(
    private fb: FormBuilder,
    private session: Store<SessionState>,
    private api: ApiService
    ) {
      this.session.select(selectSessionUser).subscribe((data) => {
        this.user = data;
        }
      );
  }

  ngOnInit() {

    this.profileForm = this.fb.group({
      publicname: [this.user.publicname],
      skype: [this.user.skype],
      telegram: [this.user.telegram],
      phone: [this.user.phone],
      about: [this.user.about],
    });



  }

  onSubmit() {
    const data = this.profileForm.value;
    const formData = new FormData();
    for(let key in data) {
      formData.append(key,data[key]);
    }
    this.api.saveProfile(formData,this.user.id).subscribe((res: any) => {
      this.session.dispatch(new sessionActions.UpdateUser(res));
    });

  }

}
