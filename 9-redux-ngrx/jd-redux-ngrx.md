# REDUX storage.

![admin]({path-to-subject}/images/111.png)

REDUX is a Predictable State Container for JS Apps

Add REDUX library ngrx to the packege.json.

      "dependencies": {
        ....
        "@ngrx/effects": "8.1.0",
        "@ngrx/entity": "8.1.0",
        "@ngrx/router-store": "8.1.0",
        "@ngrx/store": "8.1.0",
        "@ngrx/store-devtools": "8.1.0"
      },

Install it.

    npm install

Import StoreModule in the projects/mobi/src/app/app.module.ts.

    // REDUX store
    import { StoreDevtoolsModule } from '@ngrx/store-devtools';
    import { StoreModule } from '@ngrx/store';

    @NgModule({
      ...
      imports: [
        ...
        StoreModule.forRoot([]),
        StoreDevtoolsModule.instrument()

![admin]({path-to-subject}/images/1.png)

[link to the chrome plugin](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd?hl=ru)

Create a new state class for the user profile in the core/src/store/states/user.state.ts.

The structure will be the same as the server returns. 

    export interface IUserState {
        id: number;
        username: string;
        gender: string;
        birthday: string;
        main_photo: string;
    }

    export class UserState implements IUserState {
        constructor(
            public id: number = 0,
            public username: string = 'undefined',
            public gender: string = 'undefined',
            public birthday: string = 'undefined',
            public main_photo: string = 'undefined'
            ) {
        }
    }




Create a new state class (interface) for the user session core/src/store/states/session.state.ts.


    import { UserState } from './user.state';

    export interface SessionState {
        token: string;
        user: UserState;
    }

    export const defaultState = {
        token: 'undefined',
        user: new UserState()
    };


Create a reducer for the data mutation core/src/store/reducers/session.reducer.ts.


    import { LogOut } from './../actions/session.action';
    import * as Actions from '../actions/session.action';
    import {SessionState, defaultState} from '../states/session.state';

    export function SessionReducer(state: SessionState = defaultState, action: Actions.ActionsUnion) {

        switch (action.type) {

            case Actions.ActionTypes.Init:

              return {
                ...action.payload
              };

              case Actions.ActionTypes.LogIn:

                return {
                  ...action.payload
                };

            case Actions.ActionTypes.LogOut:

                return {
                    ...defaultState
                };

            default:
            return state;

        }
    }


Create an actiion by defining enum core/src/store/actions/session.action.ts.

    import { Action } from '@ngrx/store';
    import { SessionState } from './../states/session.state';

    export enum ActionTypes {
        Init = '[Session] Init user',
        LogIn = '[Session] Log in',
        LogOut = '[Session] Log out'
    }

    export class Init implements Action {
        readonly type = ActionTypes.Init;
        constructor(public payload: SessionState) {}
    }

    export class LogIn implements Action {
        readonly type = ActionTypes.LogIn;
        constructor(public payload: SessionState) {}
    }

    export class LogOut implements Action {
        readonly type = ActionTypes.LogOut;
    }

    export type ActionsUnion =
    Init |
    LogOut |
    LogIn;


Enums allow us to define a set of named constants.

Create an ActionReducerMap in the core/src/store/index.ts



    import { ActionReducerMap } from '@ngrx/store';

    import { SessionState } from './states/session.state';
    import {SessionReducer} from './reducers/session.reducer';


    export interface State {
        session: SessionState;
    }

    export const reducers: ActionReducerMap<State> = {
        session: SessionReducer,
    };


Include this ActionReducerMap into core.module.
    
    ...
    // REDUX store
    import { StoreDevtoolsModule } from '@ngrx/store-devtools';
    import { StoreModule } from '@ngrx/store';
    import { reducers } from './../store/index';

    @NgModule({
      ...
      imports: [
        ...
        StoreModule.forRoot(reducers),
        StoreDevtoolsModule.instrument()
      ],

![admin]({path-to-subject}/images/2.png)


Dispach the action from the component.

    ...
    import { Store } from '@ngrx/store';
    import * as sessionActions from '../../../store/actions/session.action';
    import { SessionState } from '../../../store/states/session.state';
    ...
    export class LoginFormComponent implements OnInit {
    ...
      constructor(
        ...
        private sessionStore: Store<SessionState>,
      ) {

      }

     ...

      onSubmit() {
        this.api.login(this.loginForm.value).subscribe((rez: any) => {
          ...
          this.sessionStore.dispatch(new sessionActions.LogIn(rez));
        }, ...)
      }

    }


![admin]({path-to-subject}/images/2.png)

![admin]({path-to-subject}/images/3.png)

Add isAuth flag into model.

    import { UserState } from './user.state';

    export interface SessionState {
        token: string;
        isAuth: boolean;
        user: UserModel;
    }

    export const defaultState = {
        token: 'undefined',
        isAuth: false,
        user: new UserModel()
    };

Set this flag in the reducer.

          case Actions.ActionTypes.LogIn:

            return {
              ...action.payload,
              isAuth: true
            };

Create a new page (main page).

Module and component.

    ng g m pages/index --project=mobi
    ng g c pages/index --project=mobi

Add a new module for the routing (mobi/src/app/pages/index/routing.ts).

    import { NgModule } from '@angular/core';
    import { Routes, RouterModule } from '@angular/router';

    import { IndexComponent } from './index.component';


    const routes: Routes = [
      {
        path: '',
        component: IndexComponent
      }
    ];

    @NgModule({
      imports: [RouterModule.forChild(routes)],
      exports: [RouterModule],
    })
    export class IndexRoutingModule {}

Add the IndexRoutingModule, IonicModule and CoreModule in the index.module.ts.


    ...

    import { IndexRoutingModule } from './routing';
    import { IonicModule } from '@ionic/angular';
    import { CoreModule } from './../../../../../core/src/lib/core.module';

    @NgModule({
      declarations: [IndexComponent],
      imports: [
        CommonModule,
        IndexRoutingModule,
        IonicModule,
        CoreModule
      ]
    })
    export class IndexModule { }

Redirect to the index module in the root routing mobi/src/app/app-routing.module.ts.

    ...
    const routes: Routes = [
      {
        path: '',
        redirectTo: 'index',
        pathMatch: 'full'
      },
      {
        path: 'index',
        loadChildren: () => import('./pages/index/index.module').then( m => m.IndexModule)
      },
    ...

Edit a template (mobi/src/app/pages/index/index.component.html).

    <ion-content [fullscreen]="true">
        <div id="container">
          <ion-card>
            <ion-card-header>
              <ion-card-title>User list</ion-card-title>
            </ion-card-header>
          
            <ion-card-content>
              
            </ion-card-content>
          </ion-card>
          </div>
    </ion-content>

Make a redirect after succesfull authorization.


    ...
    import { Router } from '@angular/router';
    ...
    export class LoginFormComponent implements OnInit {
    ...

      constructor(
        ...
        private router: Router
      ) {

      }
    ...

      onSubmit() {
        this.api.login(this.loginForm.value).subscribe((rez: any) => {
          ...
          this.router.navigate(['index']);
        }, ...)
      }

    }

Make a selector for the isAuth and session user state (core/src/store/selectors/session.selector.ts).

    import { SessionState } from '../states/session.state';
    import { createSelector, createFeatureSelector } from '@ngrx/store';

    export const getSessionStateSelector = createFeatureSelector<SessionState>('session');

    export const selectIsAuth = createSelector(
        getSessionStateSelector,
        (state: SessionState) => state.isAuth
    );

    export const selectSessionUser = createSelector(
        getSessionStateSelector,
        (state: SessionState) => state.user
    );

Select this variables from the component

    ...
    // Store
    import { SessionState } from './../../../core/src/store/states/session.state';
    import { Store } from '@ngrx/store';
    import { selectIsAuth, selectSessionUser } from './../../../core/src/store/selectors/session.selector';
    import { UserState } from './../../../core/src/store/states/user.state';

    ...
    export class AppComponent implements OnInit {
      ...
      public sessionUser: UserState;
      public isAuth: boolean;
    ...

      constructor(
        ...
        private sessionStore: Store<SessionState>,
      ) {
        this.initializeApp();

        this.sessionStore.select(selectIsAuth).subscribe(data => {
          this.isAuth = data;
        });

        this.sessionStore.select(selectSessionUser).subscribe(data => {
          this.sessionUser = data;
        });
    ...



Print the Logout link and username with photo in the sidebar mobi/src/app/app.component.html.


        <ion-list id="inbox-list">
          <ng-container *ngIf="isAuth && sessionUser">
            <ion-list-header>
              <img class="user-photo" [src]="sessionUser.main_photo" />
              {{ sessionUser.username }}
            </ion-list-header>
            <ion-note></ion-note>
          </ng-container>

          <ion-menu-toggle auto-hide="false">
            
            <ion-item  *ngIf="!isAuth" routerLink="login">
              <ion-icon slot="start" src="static/front_dist/mobi/svg/chevron-down-sharp.svg"></ion-icon>
              <ion-label>Login</ion-label>
            </ion-item>

            <ion-item *ngIf="!isAuth" routerLink="registration">
              <ion-icon slot="start" src="static/front_dist/mobi/svg/chevron-down-sharp.svg"></ion-icon>
              <ion-label>Registration</ion-label>
            </ion-item>

            <ion-item *ngIf="isAuth">
              <ion-icon slot="start" src="static/front_dist/mobi/svg/exit-sharp.svg"></ion-icon>
              <ion-label>Logout</ion-label>
            </ion-item>
          </ion-menu-toggle>
        </ion-list>

![admin]({path-to-subject}/images/4.png)




