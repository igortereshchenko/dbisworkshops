import React from "react";
import {connect} from "react-redux";
import {createStructuredSelector} from "reselect";


import {
    AdminHomeContainer,
    GraphContainer,
} from './admin-home.styles.jsx';

import './admin-home.styles.css';

import {selectCurrentUser} from "../../redux/user/user.selectors";
import {
    selectAllOrders,
    selectOrdersKeys,
    selectUsersForPreview,
    selectUsersKeys
} from "../../redux/admin/admin.selectors";
import {AdminGetOrdersStart, AdminGetUserStart} from "../../redux/admin/admin.actions";
import {
    AdminCustomButtonContainer,
    AdminHeaderContainer,
    TitleContainer
} from "../admin-all-users/admin-all-users.styles";
import {countUsersToOrders} from "../../redux/admin/admin.utils";


class AdminHome extends React.Component {
    componentDidMount() {
        const {AdminGetUserStart, AdminGetOrdersStart} = this.props;
        AdminGetOrdersStart();
        AdminGetUserStart();
    }


    render() {
        const RefreshData = () => {
            const {AdminGetUserStart, AdminGetOrdersStart} = this.props;
            AdminGetOrdersStart();
            AdminGetUserStart();
        }
        const {usersKeys, ordersKeys} = this.props;
        if (usersKeys.length !== 0 && ordersKeys !== []) {
            const usersToOrders = countUsersToOrders({usersKeys, ordersKeys})
            console.log(usersToOrders)
        }
        return (
            <AdminHomeContainer>
                <AdminHeaderContainer>
                    <TitleContainer>Главная</TitleContainer>
                    <AdminCustomButtonContainer
                        onClick={() => RefreshData()}>ОБНОВИТЬ</AdminCustomButtonContainer>
                </AdminHeaderContainer>
                <GraphContainer>
                    <div className="grid">
                        <section>
                            <svg className="circle-chart" viewBox="0 0 33.83098862 33.83098862" width="250"
                                 height="250">
                                <circle className="circle-chart__background" stroke="lightgrey" strokeWidth="2"
                                        fill="none"
                                        cx="16.91549431" cy="16.91549431" r="15.91549431"/>
                                <circle className="circle-chart__circle" stroke="#00acc1" strokeWidth="2"
                                        strokeDasharray="70,100" strokeLinecap="round" fill="none" cx="16.91549431"
                                        cy="16.91549431" r="15.91549431"/>
                                <g className="circle-chart__info">
                                    <text className="circle-chart__percent" x="16.91549431" y="15.5"
                                          alignmentBaseline="central" textAnchor="middle" fontSize="8">50%
                                    </text>
                                    <text className="circle-chart__subline" x="16.91549431" y="20.5"
                                          alignmentBaseline="central" textAnchor="middle" fontSize="2">Yay 50%
                                        progress!
                                    </text>
                                </g>
                            </svg>
                        </section>
                    </div>
                </GraphContainer>
            </AdminHomeContainer>
        )
    }
}


const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
    usersKeys: selectUsersKeys,
    ordersKeys: selectOrdersKeys,
});

const mapDispatchToProps = dispatch => ({
    AdminGetUserStart: () => dispatch(AdminGetUserStart()),
    AdminGetOrdersStart: () => dispatch(AdminGetOrdersStart()),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(AdminHome);