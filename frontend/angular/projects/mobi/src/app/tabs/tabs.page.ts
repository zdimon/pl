import { SessionService } from './../../../../core/src/lib/services/session.service';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-tabs',
  templateUrl: 'tabs.page.html',
  styleUrls: ['tabs.page.scss']
})
export class TabsPageComponent  implements OnInit{
  isAuth: boolean;

  constructor(private session: SessionService) {
    
  }

  ngOnInit() {
    this.isAuth = this.session.getIsAuth();
  }

  doLogout(){
    console.log('logout');
    this.session.logout();
  }

}
