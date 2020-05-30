import {all, call, takeLatest, put} from 'redux-saga/effects';

import UserActionTypes from '../user/user.types';
import CartActionTypes from "./cart.types";
import {clearCart, createNewOrderFailure, createNewOrderSuccess} from './cart.actions';
import {createUserOrderDocument} from "../../firebase/firebase.utils";

export function* clearCartOnSignOut() {
    yield put(clearCart());
}

export function* clearCartOnCheckout() {
    yield put(clearCart());
}

export function* createNewOrder({payload: {orderUserData, cartItems, total}}) {
    try {
        if (!orderUserData) return;
        yield createUserOrderDocument({
            orderUserData,
            cartItems,
            total
        });
        yield put(createNewOrderSuccess());
    } catch (error) {
        yield put(createNewOrderFailure(error));
    }
}

export function* onSignOutSuccess() {
    yield takeLatest(UserActionTypes.SIGN_OUT_SUCCESS, clearCartOnSignOut);
}

export function* onCheckoutSuccess() {
    yield takeLatest(CartActionTypes.CREATE_NEW_ORDER_SUCCESS, clearCartOnCheckout);
}

export function* onCreateNewOrderStart() {
    yield takeLatest(CartActionTypes.CREATE_NEW_ORDER_START, createNewOrder);
}

export function* cartSagas() {
    yield all([
        call(onSignOutSuccess),
        call(onCheckoutSuccess),
        call(onCreateNewOrderStart),
    ]);
}
