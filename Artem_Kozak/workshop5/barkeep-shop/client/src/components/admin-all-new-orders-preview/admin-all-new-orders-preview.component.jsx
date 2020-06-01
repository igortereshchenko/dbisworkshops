import React from "react";
import {connect} from "react-redux";
import {createStructuredSelector} from "reselect";

import {} from './admin-all-new-orders-preview.styles';
import {AdminNewOrdersContainer, TitleContainer} from "../admin-new-orders/admin-new-orders.styles";
import {selectOrdersForPreview} from "../../redux/admin/admin.selectors";
import AdminNewOrders from "../admin-new-orders/admin-new-orders.component";
import {AdminGetOrdersStart} from "../../redux/admin/admin.actions";

import {
    AdminCustomButtonContainer,
    AdminHeaderContainer
} from "../admin-all-users/admin-all-users.styles";

class AdminAllNewOrdersPreview extends React.Component {
    componentDidMount() {
        const {AdminGetOrdersStart} = this.props;
        AdminGetOrdersStart();
    }

    render() {
        return (
            <AdminNewOrdersContainer>
                <AdminHeaderContainer>
                    <TitleContainer>Новые заказы</TitleContainer>
                    <AdminCustomButtonContainer
                        onClick={() => this.props.AdminGetOrdersStart()}>ОБНОВИТЬ</AdminCustomButtonContainer>
                </AdminHeaderContainer>
                {
                    this.props.userOrders ? (this.props.userOrders
                            .sort((a, b) => b.createdAt.seconds - a.createdAt.seconds)
                            .map(order => (
                                <AdminNewOrders key={order.id} orderId={order.id} orderProps={order}/>
                            ))
                    ) : null
                }
            </AdminNewOrdersContainer>
        );
    }

}


const mapStateToProps = createStructuredSelector({
    userOrders: selectOrdersForPreview
});

const mapDispatchToProps = dispatch => ({
    AdminGetOrdersStart: () => dispatch(AdminGetOrdersStart())
});

export default connect(mapStateToProps, mapDispatchToProps)(AdminAllNewOrdersPreview);