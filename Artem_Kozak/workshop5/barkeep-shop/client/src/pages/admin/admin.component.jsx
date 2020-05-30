import React from 'react'
import {connect} from "react-redux";
import {Route, Switch} from 'react-router-dom';

import {
    AdminPageContainer
} from './admin.styles';
import AdminNavigation from "../../components/admin-navigation/admin-navigation.component";
import {Line} from "../profile/profile.styles";
import AdminAllUsers from "../../components/admin-all-users/admin-all-users.component";
import AdminAllNewOrdersPreview
    from "../../components/admin-all-new-orders-preview/admin-all-new-orders-preview.component";

const AdminPage = () => {
    return (
        <AdminPageContainer>
            <AdminNavigation/>
            <Line/>
            <Switch>
                <Route exact path='/administrator_page_for_user_orders_and_other'
                       component={AdminAllNewOrdersPreview}/>
                <Route exact path='/administrator_page_for_user_orders_and_other/new-orders'
                       component={AdminAllNewOrdersPreview}/>
                <Route exact path='/administrator_page_for_user_orders_and_other/completed-orders'
                       component={AdminAllNewOrdersPreview}/>
                <Route exact path='/administrator_page_for_user_orders_and_other/users'
                       component={AdminAllUsers}/>
            </Switch>
            <Line/>
        </AdminPageContainer>
    )
};

const mapStateToProps = () => ({});

export default connect(mapStateToProps)(AdminPage);