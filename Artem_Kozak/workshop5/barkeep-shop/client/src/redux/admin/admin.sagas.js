import {
    all,
    call, takeLatest, put
} from 'redux-saga/effects';

import AdminActionTypes from "./admin.types";
import {
    AdminGetUserSuccess,
    AdminGetUserFailure,
    AdminGetOrdersSuccess,
    AdminGetOrdersFailure,
    AdminUpdateOrderStatusSuccess, AdminUpdateOrderStatusFailure
} from "./admin.actions";
import {
    firestore,
    convertUsersSnapshotToMap,
    convertAdminUsersOrdersSnapshotToMap, updateAdminUserStatusDocument
} from '../../firebase/firebase.utils';


export function* adminAllGetUsers() {
    try {
        const usersRef = yield firestore.collection('users')
        const snapShot = yield usersRef.get();
        const usersMap = yield call(
            convertUsersSnapshotToMap,
            snapShot
        );
        yield put(AdminGetUserSuccess(usersMap))
    } catch (error) {
        yield put(AdminGetUserFailure(error))
    }
}

export function* AdminGetAllOrders() {
    try {
        const ordersRef = yield firestore.collectionGroup('orders')
        const snapShot = yield ordersRef.get();
        const ordersMap = yield call(
            convertAdminUsersOrdersSnapshotToMap,
            snapShot
        );
        yield put(AdminGetOrdersSuccess(ordersMap))
    } catch (error) {
        yield put(AdminGetOrdersFailure(error))
    }
}

export function* AdminUpdateOrderStatus({payload: {userId, orderId, orderStatus}}) {
    try {
        yield updateAdminUserStatusDocument({userId, orderId, orderStatus});
        yield put(AdminUpdateOrderStatusSuccess())
    } catch (error) {
        yield put(AdminUpdateOrderStatusFailure(error))
    }
}


export function* onAdminGetUser() {
    yield takeLatest(
        AdminActionTypes.ADMIN_GET_ALL_USERS_START,
        adminAllGetUsers
    );
}

export function* onAdminGetAllOrdersStart() {
    yield takeLatest(
        AdminActionTypes.ADMIN_GET_ALL_ORDERS_START,
        AdminGetAllOrders
    );
}

export function* onAdminUpdateOrderStatusStart() {
    yield takeLatest(
        AdminActionTypes.ADMIN_UPDATE_ORDER_STATUS_START,
        AdminUpdateOrderStatus
    );
}


export function* adminSagas() {
    yield all([
        call(onAdminGetUser),
        call(onAdminGetAllOrdersStart),
        call(onAdminUpdateOrderStatusStart),
    ]);
}

