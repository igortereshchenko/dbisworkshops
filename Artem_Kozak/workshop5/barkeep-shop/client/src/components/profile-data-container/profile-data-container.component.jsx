import React from "react";
import shortid from 'shortid';

import ProfileAddDataButton from "../profile-add-data-button/profile-add-data-button.component";

import {
    FlexTextsContainer,
    LabelContainer,
    TextContainer,
    UserDataContainer
} from './profile-data-container.styles';
import {formatPhoneNumberIntl} from "react-phone-number-input";

const UserData = (props) => (
    <UserDataContainer>
        <LabelContainer>{props.label}</LabelContainer>
        <FlexTextsContainer>
            {
                props.otherText[0] === null ? (
                    <TextContainer as='div'>
                        <ProfileAddDataButton/>
                    </TextContainer>
                ) : props.phones ? (
                    props.otherText.map((phone) => (
                        <TextContainer key={shortid.generate()}>{formatPhoneNumberIntl(phone)}</TextContainer>
                    ))
                ) : (
                    props.otherText.map((text) => (
                        <TextContainer key={shortid.generate()}>{text}</TextContainer>
                    ))
                )
            }
            {
                props.canAdd && (props.otherText[0] !== null) ? (
                    <TextContainer as='div'>
                        <ProfileAddDataButton/>
                    </TextContainer>
                ) : null
            }
        </FlexTextsContainer>
    </UserDataContainer>
);

export default UserData;