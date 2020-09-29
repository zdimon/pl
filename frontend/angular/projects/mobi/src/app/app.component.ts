import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

// Store 

import { Store } from '@ngrx/store';
import { SessionState } from './../../../core/src/lib/store/states/session.state';
import { selectSessionUser, selectIsAuth } from './../../../core/src/lib/store/selectors/session.selector';
import * as sessionActions from './../../../core/src/lib/store/actions/session.action';

import { CategoryListState } from './../../../core/src/lib/store/states/category.state';
import { selectCategory } from './../../../core/src/lib/store/selectors/catalog.selector';

// Services
import { ApiService } from './../../../core/src/lib/services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {

  categories: Observable<any>;
  isAuth: Observable<boolean>;
  user: any;


  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private api: ApiService,
    private session: Store<SessionState>,
    private categoryState: Store<CategoryListState>
  ) {
    this.initializeApp();
    this.categories = this.categoryState.select(selectCategory);
    this.user = this.session.select(selectSessionUser);
    this.isAuth = this.session.select(selectIsAuth);
  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  doSelectFilter(id: number){
    this.api.setFilter(id).subscribe((data: any) => {
      console.log(data);
    })
  }
}
