import React from "react";
import WithSpinner from "../with-spinner/with-spinner.component";
import PersonalInformation from "./profile-personal-information.component";
import {createStructuredSelector} from "reselect";
import {selectCurrentUser} from "../../redux/user/user.selectors";
import {connect} from "react-redux";

import {ProfileDataContainer} from "../../pages/profile/profile.styles";

const PersonalInformationWithSpinner = WithSpinner(PersonalInformation);

const PersonalInformationContainerPage = ({currentUser}) => (
    <ProfileDataContainer>
        <PersonalInformationWithSpinner isLoading={!currentUser} currentUser={currentUser}/>
    </ProfileDataContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
});

export default connect(
    mapStateToProps,
    null
)(PersonalInformationContainerPage);