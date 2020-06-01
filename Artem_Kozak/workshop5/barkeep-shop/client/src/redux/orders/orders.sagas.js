import {all, call, put, takeLatest} from 'redux-saga/effects';

import {convertUserOrdersSnapshotToMap, firestore} from '../../firebase/firebase.utils';

import {fetchUserOrdersFailure, fetchUserOrdersSuccess} from './orders.actions';

import OrdersActionTypes from './orders.types';

export function* fetchUserOrdersAsync({payload: {id}}) {
    try {
        const userOrderRef = yield firestore.collection(`users/${id}/orders`);
        const snapShot = yield userOrderRef.get();
        const ordersMap = yield call(
            convertUserOrdersSnapshotToMap,
            snapShot
        );
        yield put(fetchUserOrdersSuccess(ordersMap));
    } catch (error) {
        yield put(fetchUserOrdersFailure(error.message));
    }
}

export function* onFetchUserOrdersStart() {
    yield takeLatest(
        OrdersActionTypes.FETCH_USER_ORDERS_START,
        fetchUserOrdersAsync
    );
}

export function* ordersSagas() {
    yield all([call(onFetchUserOrdersStart)]);
}
