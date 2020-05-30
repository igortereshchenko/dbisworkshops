import React from "react";

import {
    AdminUserBlock,
    AdminUserBody,
    AdminUserDataText,
    AdminUserFooter,
    AdminUserHead,
    AdminUserInformation,
    ImageContainer
} from './admin-user-item.styles';

import {
    BackgroundImage,
    DefaultBackgroundImage
} from "../profile-personal-information/profile-personal-information.styles";

const AdminUserItem = ({user}) => {
    return (
        <AdminUserBlock>
            <AdminUserHead className={user.address ? 'green' : 'orange'}>
                <ImageContainer>
                    {user.photoURL ? (
                        <BackgroundImage photoURL={user.photoURL}/>
                    ) : (
                        <DefaultBackgroundImage/>
                    )}
                </ImageContainer>
            </AdminUserHead>
            <AdminUserBody>
                <AdminUserDataText>
                    <p>Имя</p>
                    <p>{user.displayName}</p>
                </AdminUserDataText>
                <AdminUserDataText>
                    <p>Почта</p>
                    <p>{user.email}</p>
                </AdminUserDataText>
                <AdminUserDataText>
                    <p>Телефон</p>
                    <p>{user.phoneNumber}</p>
                </AdminUserDataText>
                <AdminUserDataText>
                    <p>Адрес</p>
                    <p>{user.address}</p>
                </AdminUserDataText>
            </AdminUserBody>
            <AdminUserFooter>
                <AdminUserInformation
                    // onClick={() => history.push(`${match.path}/${routeName}`)}
                >
                    <span>&#10095;</span>
                </AdminUserInformation>
            </AdminUserFooter>
        </AdminUserBlock>
    );
}

export default AdminUserItem;