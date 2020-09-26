
import { SessionService } from './../../../../core/src/lib/services/session.service';
import { Component, OnInit } from '@angular/core';


// Store
import { SessionState } from './../../../../core/src/lib/store/states/session.state';
import { Store } from '@ngrx/store';
import { selectIsAuth, selectSessionUser } from './../../../../core/src/lib/store/selectors/session.selector';
import { UserState } from './../../../../core/src/lib/store/states/user.state';
////

@Component({
  selector: 'app-tabs',
  templateUrl: 'tabs.page.html',
  styleUrls: ['tabs.page.scss']
})
export class TabsPageComponent  implements OnInit{
  isAuth: boolean;

  constructor(
    private session: SessionService,
    private sessionStore: Store<SessionState>
    ) {
    
  }

  ngOnInit() {
    //this.isAuth = this.session.getIsAuth();
    this.sessionStore.select(selectIsAuth).subscribe((data: boolean) => {
      this.isAuth = data;
    });
  }

  doLogout(){
    console.log('logout');
    this.session.logout();
  }

}
