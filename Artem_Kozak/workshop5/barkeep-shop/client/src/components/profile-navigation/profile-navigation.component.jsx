import React from "react";

import {NavigationContainer, NavigationProfileLink} from './profile-navigation.styles';

const ProfileNavigation = () => (
    <NavigationContainer>
        <NavigationProfileLink to='/profile/personal-information/'>Главная</NavigationProfileLink>
        <NavigationProfileLink to='/profile/loyalty/'>Бонусные баллы</NavigationProfileLink>
        <NavigationProfileLink to='/profile/orders-history/'>История заказов</NavigationProfileLink>
    </NavigationContainer>
);

export default ProfileNavigation;