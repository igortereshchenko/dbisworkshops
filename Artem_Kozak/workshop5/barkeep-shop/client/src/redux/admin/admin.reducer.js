import AdminActionTypes from "./admin.types";

const INITIAL_STATE = {
    users: null,
    error: null,
    orders: null,
};

const adminReducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case AdminActionTypes.ADMIN_GET_ALL_ORDERS_START:
        case AdminActionTypes.ADMIN_GET_ALL_USERS_START:
        case AdminActionTypes.ADMIN_UPDATE_ORDER_STATUS_START:
            return {
                ...state,
                error: null,
            }
        case AdminActionTypes.ADMIN_GET_ALL_ORDERS_SUCCESS:
            return {
                ...state,
                orders: action.payload,
                error: null,
            };
        case AdminActionTypes.ADMIN_GET_ALL_USERS_SUCCESS:
            return {
                ...state,
                users: action.payload,
                error: null,
            };
        case AdminActionTypes.ADMIN_GET_ALL_USERS_ORDERS_SUCCESS:
            return {
                ...state,
                error: null,
            };
        case AdminActionTypes.ADMIN_UPDATE_ORDER_STATUS_FAILURE:
        case AdminActionTypes.ADMIN_GET_ALL_USERS_FAILURE:
        case AdminActionTypes.ADMIN_GET_ALL_ORDERS_FAILURE:
        case AdminActionTypes.ADMIN_GET_ALL_USERS_ORDERS_FAILURE:
            return {
                ...state,
                error: action.payload,
            }
        default:
            return state;
    }
};

export default adminReducer;
