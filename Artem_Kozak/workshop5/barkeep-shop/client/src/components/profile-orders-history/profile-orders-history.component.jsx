import React from 'react';
import {connect} from 'react-redux';
import {createStructuredSelector} from "reselect";

import {fetchUserOrdersStart} from "../../redux/orders/orders.actions";
import {selectCurrentUser} from "../../redux/user/user.selectors";
import {selectUserOrdersForPreview} from "../../redux/orders/orders.selectors";

import UserData from "../profile-data-container/profile-data-container.component";

import {
    PersonalInformationContainer,
    TitleContainer
} from '../profile-personal-information/profile-personal-information.styles';
import OrderItemList from "../order-item-list/order-item-list.component";

class OrdersHistory extends React.Component {
    componentDidMount() {
        const {fetchUserOrdersStart} = this.props;

        fetchUserOrdersStart(this.props.currentUser.id);
    }

    render() {
        return (
            <PersonalInformationContainer>
                <TitleContainer>История Ваших заказов</TitleContainer>
                {
                    this.props.userOrders ? (
                        this.props.userOrders
                            .sort((a, b) => b.createdAt.seconds - a.createdAt.seconds)
                            .map(({id, ...otherOrderProps}) => (
                                <OrderItemList key={id} orderId={id} {...otherOrderProps}/>
                            ))
                    ) : (
                        <UserData
                            label={"Упс"}
                            otherText={["Кажется Вы еще у нас не заказывали... Может время сделать Ваш первый заказ?"]}
                            loyalty={true}
                        />
                    )

                }

            </PersonalInformationContainer>
        )
    };
}


const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
    userOrders: selectUserOrdersForPreview,
});

const mapDispatchToProps = dispatch => ({
    fetchUserOrdersStart: id => dispatch(fetchUserOrdersStart({id}))
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(OrdersHistory);
