

import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

// Store
import { Store } from '@ngrx/store';
import { SessionState } from './../../store/states/session.state';
import { selectSessionUser } from './../../store/selectors/session.selector';

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
      email: [this.user.username],
      skype: [this.user.skype],
      telegram: [this.user.telegram],
      phone: [this.user.phone],
      about: [this.user.about],
    });



  }

  onSubmit() {
    const data = this.profileForm.value;
    data.id = this.user.id;
    this.api.saveProfile(data).subscribe((res: any) => {
      console.log(res);
    });

  }

}
