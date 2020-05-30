import React from "react";
import WithSpinner from "../with-spinner/with-spinner.component";
import {createStructuredSelector} from "reselect";
import {selectCurrentUser} from "../../redux/user/user.selectors";
import {connect} from "react-redux";

import Loyalty from "./profile-loyalty.component";
import {ProfileDataContainer} from "../../pages/profile/profile.styles";

const LoyaltyWithSpinner = WithSpinner(Loyalty);

const LoyaltyContainerPage = ({currentUser}) => (
    <ProfileDataContainer>
        <LoyaltyWithSpinner isLoading={!currentUser} currentUser={currentUser}/>
    </ProfileDataContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
});

export default connect(
    mapStateToProps,
    null
)(LoyaltyContainerPage);