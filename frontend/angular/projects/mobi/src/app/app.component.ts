
import { Component } from '@angular/core';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

// Store 

import { Store } from '@ngrx/store';
import { SessionState } from './../../../core/src/lib/store/states/session.state';
import { selectSessionUser } from './../../../core/src/lib/store/selectors/session.selector';
import * as sessionActions from './../../../core/src/lib/store/actions/session.action';

import { ApiService } from './../../../core/src/lib/services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {

  categories: any;
  user: any;


  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private api: ApiService,
    private session: Store<SessionState>,
  ) {
    this.initializeApp();
    this.api.getCategoryList().subscribe((data: any) => {
      this.categories = data;
    });
    this.user = this.session.select(selectSessionUser);
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }
}
