import {createSelector} from 'reselect';

const selectOrders = state => state.orders;

export const selectUserOrders = createSelector(
    [selectOrders],
    orders => orders.userOrders
);

export const selectUserOrdersForPreview = createSelector(
    [selectUserOrders],
    userOrders => userOrders ? Object.keys(userOrders).map(key => userOrders[key]) : []
);

export const selectUserOrder = userOrderUrlParam => createSelector(
    [selectUserOrders],
    userOrders => (userOrders ? userOrders[userOrderUrlParam] : null)
);

export const selectOrderItemsCount = createSelector(
    [selectUserOrders],
    orderItems =>
        orderItems.reduce(
            (accumulatedQuantity, orderItem) =>
                accumulatedQuantity + orderItem.quantity,
            0
        )
);

export const selectIsUserOrderFetching = createSelector(
    [selectOrders],
    orders => orders.isFetching
);

export const selectIsUserOrdersLoaded = createSelector(
    [selectOrders],
    orders => !!orders.userOrders
);

export const selectOrderHidden = createSelector(
    [selectOrders],
    orders => orders.selected
);
