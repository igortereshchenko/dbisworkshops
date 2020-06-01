import CartActionTypes from './cart.types';

export const toggleCartHidden = () => ({
    type: CartActionTypes.TOGGLE_CART_HIDDEN
});

export const addItem = item => ({
    type: CartActionTypes.ADD_ITEM,
    payload: item
});

export const removeItem = item => ({
    type: CartActionTypes.REMOVE_ITEM,
    payload: item
});

export const clearItemFromCart = item => ({
    type: CartActionTypes.CLEAR_ITEM_FROM_CART,
    payload: item
});

export const createNewOrderStart = orderData => ({
    type: CartActionTypes.CREATE_NEW_ORDER_START,
    payload: orderData
});

export const createNewOrderSuccess = () => ({
    type: CartActionTypes.CREATE_NEW_ORDER_SUCCESS,
});

export const createNewOrderFailure = error => ({
    type: CartActionTypes.CREATE_NEW_ORDER_SUCCESS,
    payload: error
});


export const clearCart = () => ({
    type: CartActionTypes.CLEAR_CART
});
