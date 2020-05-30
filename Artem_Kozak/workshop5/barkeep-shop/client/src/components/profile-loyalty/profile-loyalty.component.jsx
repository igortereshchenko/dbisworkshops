import React from "react";

import UserData from "../profile-data-container/profile-data-container.component";

import {
    PersonalInformationContainer,
    TitleContainer
} from '../profile-personal-information/profile-personal-information.styles';

const Loyalty = ({currentUser}) => (
    <PersonalInformationContainer>
        <TitleContainer>Программа лояльности</TitleContainer>
        <UserData label={"У Вас накоплено"} otherText={[currentUser.loyaltyPoints + ' бонусных грн']} loyalty={true}/>
    </PersonalInformationContainer>
);

export default Loyalty;