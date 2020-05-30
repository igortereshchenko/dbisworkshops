import React from 'react'
import {Route, Switch} from 'react-router-dom'

import ProfileNavigation from "../../components/profile-navigation/profile-navigation.component";
import PersonalInformationContainerPage
    from "../../components/profile-personal-information/profile-personal-information.container";
import LoyaltyContainerPage from "../../components/profile-loyalty/profile-loyalty.container";
import OrdersHistoryContainerPage from "../../components/profile-orders-history/profile-orders-history.container";

import {Line, ProfilePageContainer} from './profile.styles';

const ProfilePage = () => {
    return (
        <ProfilePageContainer>
            <ProfileNavigation/>
            <Line/>
            <Switch>
                <Route exact path='/profile'
                       component={PersonalInformationContainerPage}/>
                <Route exact path='/profile/personal-information/'
                       component={PersonalInformationContainerPage}/>
                <Route exact path='/profile/loyalty' component={LoyaltyContainerPage}/>
                <Route exact path='/profile/orders-history' component={OrdersHistoryContainerPage}/>
            </Switch>
            <Line/>
        </ProfilePageContainer>
    )
};

export default ProfilePage;