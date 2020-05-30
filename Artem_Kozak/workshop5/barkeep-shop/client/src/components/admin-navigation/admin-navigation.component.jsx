import React from "react";

import {NavigationContainer, NavigationProfileLink} from './admin-navigation.styles';

const AdminNavigation = () => (
    <NavigationContainer>
        <NavigationProfileLink to='/administrator_page_for_user_orders_and_other/'>
            Главная
        </NavigationProfileLink>
        <NavigationProfileLink to='/administrator_page_for_user_orders_and_other/new-orders'>
            Новые заказы
        </NavigationProfileLink>
        <NavigationProfileLink to='/administrator_page_for_user_orders_and_other/completed-orders'>
            Выполненные заказы
        </NavigationProfileLink>
        <NavigationProfileLink to='/administrator_page_for_user_orders_and_other/users'>
            Пользователи
        </NavigationProfileLink>
    </NavigationContainer>
);

export default AdminNavigation;