


import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { HttpClientModule } from '@angular/common/http';

import {MatExpansionModule} from '@angular/material/expansion';
import { AuthGuard } from './guards/auth.guard';
import { SessionService } from './../../../core/src/lib/services/session.service';


import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { StoreModule } from '@ngrx/store';

import { reducers } from './../../../core/src/lib/store/index';

import { APP_INITIALIZER } from '@angular/core';

import { InitService } from './../../../core/src/lib/services/init.service';

export function init_app(initService: InitService) {
  return () => initService.init();
}

import { HTTP_INTERCEPTORS } from '@angular/common/http';

import { AuthInterceptor } from './../../../core/src/lib/interceptors/auth.interceptor';

export const interceptorProviders = [
  { 
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  }
];



@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatExpansionModule,
    StoreModule.forRoot(reducers),
    StoreDevtoolsModule.instrument()
  ],
  providers: [
    interceptorProviders,
    {
      provide: APP_INITIALIZER,
      useFactory: init_app,
      deps: [InitService],
      multi: true,
    },
    StatusBar,
    SplashScreen,
    AuthGuard,
    SessionService,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
