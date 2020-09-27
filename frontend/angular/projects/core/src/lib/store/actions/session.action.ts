import { Action } from '@ngrx/store';
import { UserState } from '../states/user.state';
import { SessionState } from './../states/session.state';

export enum ActionTypes {
    Init = '[Session] Init user',
    LogIn = '[Session] Log in',
    LogOut = '[Session] Log out',
    UpdateUser = '[Session] Update user'
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

export class UpdateUser implements Action {
    readonly type = ActionTypes.UpdateUser;
    constructor(public payload: UserState) {}
}

export type ActionsUnion =
Init |
LogOut |
UpdateUser |
LogIn;
