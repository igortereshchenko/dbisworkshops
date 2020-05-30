import React from "react";

import {
    ProfileAddDataButtonContainer,
    AddButton
} from './profile-add-data-button.styles';

const ProfileAddDataButton = () => (
    <ProfileAddDataButtonContainer>
        <AddButton>
            <span>&#43;</span>
            добавить
        </AddButton>
    </ProfileAddDataButtonContainer>
);

export default ProfileAddDataButton;