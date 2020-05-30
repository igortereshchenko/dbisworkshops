import React from "react";
import WithSpinner from "../with-spinner/with-spinner.component";
import {createStructuredSelector} from "reselect";
import {selectCurrentUser} from "../../redux/user/user.selectors";
import {connect} from "react-redux";

import OrdersHistory from "./profile-orders-history.component";
import {ProfileDataContainer} from "../../pages/profile/profile.styles";

const OrdersHistoryWithSpinner = WithSpinner(OrdersHistory);

const OrdersHistoryContainerPage = ({currentUser}) => (
    <ProfileDataContainer>
        <OrdersHistoryWithSpinner
            isLoading={!currentUser}
        />
    </ProfileDataContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
});

export default connect(
    mapStateToProps,
    null
)(OrdersHistoryContainerPage);