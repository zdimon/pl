import { UserState } from './../states/user.state';
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

export const selectUserId = createSelector(
    selectSessionUser,
    (user: UserState) => user.id
);

export const selectUserFilter = createSelector(
    getSessionStateSelector,
    (state: SessionState) => state.filter
);