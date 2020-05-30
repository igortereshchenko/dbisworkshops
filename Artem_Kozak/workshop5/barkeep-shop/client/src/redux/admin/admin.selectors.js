import {createSelector} from 'reselect';

const selectAdmin = state => state.admin;

export const selectAllUsers = createSelector(
    [selectAdmin],
    admin => admin.users
);

export const selectUsersForPreview = createSelector(
    [selectAllUsers],
    users => users ? Object.keys(users).map(key => users[key]) : []
);

export const selectAllOrders = createSelector(
    [selectAdmin],
    admin => admin.orders
);

export const selectOrdersForPreview = createSelector(
    [selectAllOrders],
    orders => orders ? Object.keys(orders).map(key => orders[key]) : []
);
