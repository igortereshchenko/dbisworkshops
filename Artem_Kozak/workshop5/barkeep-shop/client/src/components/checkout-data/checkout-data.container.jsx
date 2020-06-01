import React from "react";
import WithSpinner from "../with-spinner/with-spinner.component";
import {createStructuredSelector} from "reselect";
import {connect} from "react-redux";

import {selectCurrentUser} from "../../redux/user/user.selectors";

import CheckoutDataBlock from "./checkout-data.component";
import {CheckoutDataContainer} from "./checkout-data.styles";

const CheckoutDataBlockWithSpinner = WithSpinner(CheckoutDataBlock);

const CheckoutDataBlockContainerPage = ({currentUser}) => (
    <CheckoutDataContainer>
        <CheckoutDataBlockWithSpinner isLoading={!currentUser} currentUser={currentUser}/>
    </CheckoutDataContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
});

export default connect(
    mapStateToProps,
    null
)(CheckoutDataBlockContainerPage);