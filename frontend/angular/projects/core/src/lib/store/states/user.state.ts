export interface IUserSatate {
    id: number;
    username: string;
}

export class UserState implements IUserSatate {
    constructor(
        public id: number = 0,
        public username: string = 'undefined') {

    }
}