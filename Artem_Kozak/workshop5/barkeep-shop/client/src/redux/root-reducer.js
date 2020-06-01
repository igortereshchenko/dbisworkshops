import {combineReducers} from 'redux';
import {persistReducer} from 'redux-persist';
import storage from 'redux-persist/lib/storage';

import userReducer from './user/user.reducer';
import cartReducer from './cart/cart.reducer';
import directoryReducer from './directory/directory.reducer';
import shopReducer from './shop/shop.reducer';
import sidebarReducer from "./sidebar/sidebar.reducer";
import profileReducer from "./profile/profile.reducer";
import ordersReducer from "./orders/orders.reducer";
import adminReducer from "./admin/admin.reducer";


const persistConfig = {
    key: 'root',
    storage,
    whitelist: ['cart']
};

const rootReducer = combineReducers({
    user: userReducer,
    cart: cartReducer,
    admin: adminReducer,
    orders: ordersReducer,
    directory: directoryReducer,
    shop: shopReducer,
    sidebar: sidebarReducer,
    profile: profileReducer
});

export default persistReducer(persistConfig, rootReducer);
