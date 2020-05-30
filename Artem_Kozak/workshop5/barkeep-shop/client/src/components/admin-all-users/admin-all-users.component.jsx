import React from "react";
import {connect} from "react-redux";
import {createStructuredSelector} from "reselect";
import {withRouter} from "react-router-dom";

import {selectCurrentUser} from "../../redux/user/user.selectors";
import {AdminGetUserStart} from "../../redux/admin/admin.actions";

import {
    AdminAllUsersContainer,
    TitleContainer,
    AdminHeaderContainer,
    AdminCustomButtonContainer,
} from './admin-all-users.styles';


import {selectUsersForPreview} from "../../redux/admin/admin.selectors";
import AdminUserItem from "../admin-user-item/admin-user-item.component";


class AdminAllUsers extends React.Component {
    componentDidMount() {
        const {AdminGetUserStart} = this.props;
        AdminGetUserStart();
    }

    render() {
        const {allUsers} = this.props;
        return (
            <AdminAllUsersContainer>
                <AdminHeaderContainer>
                    <TitleContainer>Пользователи</TitleContainer>
                    <AdminCustomButtonContainer
                        onClick={() => this.props.AdminGetUserStart()}>ОБНОВИТЬ</AdminCustomButtonContainer>
                </AdminHeaderContainer>
                {
                    allUsers.length > 0  ? (
                        allUsers.sort((a, b) => b.createdAt.seconds - a.createdAt.seconds).map(user => (
                            <AdminUserItem key={user.id} user={user}/>
                        ))
                    ) : (
                        <p>обновите список</p>
                    )
                }
            </AdminAllUsersContainer>
        );
    };
}

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
    allUsers: selectUsersForPreview,
});

const mapDispatchToProps = dispatch => ({
    AdminGetUserStart: () => dispatch(AdminGetUserStart()),
});

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(AdminAllUsers));