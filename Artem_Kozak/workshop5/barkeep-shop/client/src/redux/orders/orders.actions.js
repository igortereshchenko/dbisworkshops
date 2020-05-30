import OrdersActionTypes from './orders.types';

export const fetchUserOrdersStart = currentUser => ({
    type: OrdersActionTypes.FETCH_USER_ORDERS_START,
    payload: currentUser
});

export const fetchUserOrdersSuccess = userOrdersMap => ({
    type: OrdersActionTypes.FETCH_USER_ORDERS_SUCCESS,
    payload: userOrdersMap
});

export const fetchUserOrdersFailure = errorMessage => ({
    type: OrdersActionTypes.FETCH_USER_ORDERS_FAILURE,
    payload: errorMessage
});

export const setOrderHidden = orderId => ({
    type: OrdersActionTypes.SET_ORDER_HIDDEN,
    payload: orderId
})