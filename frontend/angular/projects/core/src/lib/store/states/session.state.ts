import { UserState } from './user.state';


export class SessionState {
    token: string;
    isAuth: boolean;
    user: UserState;
}

export const defaultState = {
    token: 'undefined',
    isAuth: false,
    user: new UserState()
}