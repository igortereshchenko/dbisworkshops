import OrdersActionTypes from './orders.types';

const INITIAL_STATE = {
    userOrders: null,
    isFetching: false,
    errorMessage: undefined,
    selected: null,
};

const ordersReducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case OrdersActionTypes.SET_ORDER_HIDDEN:
            return {
                ...state,
                selected: action.payload,
            }
        case OrdersActionTypes.FETCH_USER_ORDERS_START:
            return {
                ...state,
                isFetching: true
            };
        case OrdersActionTypes.FETCH_USER_ORDERS_SUCCESS:
            return {
                ...state,
                isFetching: false,
                userOrders: action.payload,
                errorMessage: undefined
            };
        case OrdersActionTypes.FETCH_USER_ORDERS_FAILURE:
            return {
                ...state,
                isFetching: false,
                errorMessage: action.payload
            };
        default:
            return state;
    }
};

export default ordersReducer;
