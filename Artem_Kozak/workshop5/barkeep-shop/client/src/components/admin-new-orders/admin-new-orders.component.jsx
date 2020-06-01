import React, {useState} from 'react';
import {connect} from 'react-redux';
import {createStructuredSelector} from "reselect";

import {
    AdminOrderContainer,
    UserInformation,
    AdminDataContainer,
    AdminImageAndStatus,
    AdminOrderStatusContainer,
    AdminCartItemsContainer,
    AdminScrollData,
    AdminOrderControlButtons,
    AdminCartItems,
    FormContainer,
    CustomButtonForm,
    DataContainer,
    StatusText
} from './admin-new-orders.styles';


import FormInput from "../form-input/form-input.component";
import CustomButton from "../custom-button/custom-button.component";
import {selectProfileUpdateHidden} from "../../redux/profile/profile.selectors";
import {toggleUpdateHidden} from "../../redux/profile/profile.actions";
import {userUpdateStart} from "../../redux/user/user.actions";
import UserData from "../profile-data-container/profile-data-container.component";
import OrderFixedItem from "../checkout-fixed-item/checkout-fixed-item.component";
import {TotalContainer} from "../checkout-data/checkout-data.styles";
import {selectOrdersForPreview, selectUsersForPreview} from "../../redux/admin/admin.selectors";
import {AdminGetOrdersStart, AdminUpdateOrderStatusStart} from "../../redux/admin/admin.actions";


const AdminNewOrders = ({orderId, orderProps, userUpdateStart, toggleUpdateHidden, profileUpdateHidden,
                            allUsers, AdminUpdateOrderStatusStart, AdminGetOrdersStart}) => {
    const [userCredentials, setCredentials] = useState({
        displayName: `${orderProps.currentUser.displayName}`,
        email: `${orderProps.currentUser.email}`,
        phoneNumber: `${orderProps.currentUser.phoneNumber == null ? '+380' : orderProps.currentUser.phoneNumber}`,
        address: `${orderProps.currentUser.address == null ? '' : orderProps.currentUser.address}`
    });

    const {displayName, email, phoneNumber, address} = userCredentials;

    const handleSubmit = async event => {
        event.preventDefault();
        userUpdateStart(displayName, email, phoneNumber, address);
        toggleUpdateHidden();
    };

    const handleChange = event => {
        const {value, name} = event.target;

        setCredentials({...userCredentials, [name]: value});
    };

    const IncreaseStatus = async event => {
        AdminUpdateOrderStatusStart(orderProps.currentUser.uid, orderId, orderProps.orderStatus + 1);
        AdminGetOrdersStart();
    };

    const DecreaseStatus = async event => {
        AdminUpdateOrderStatusStart(orderProps.currentUser.uid, orderId, orderProps.orderStatus - 1);
        AdminGetOrdersStart();
    };

    return (
        <AdminOrderContainer>
            <UserInformation>
                <AdminImageAndStatus>
                    <AdminOrderStatusContainer>
                        {
                            orderProps.orderStatus <= -1 ? (
                                <StatusText className={'red'}>Отменен</StatusText>
                            ) : orderProps.orderStatus === 0 ? (
                                <StatusText className={'orange'}>Новый заказ</StatusText>
                            ) : orderProps.orderStatus === 1 ? (
                                <StatusText className={'gray'}>Обработан</StatusText>
                            ) : orderProps.orderStatus === 2 ? (
                                <StatusText className={'gray'}>Доставляется</StatusText>
                            ) : orderProps.orderStatus >= 3 ? (
                                <StatusText className={'green'}>Выполнен</StatusText>
                            ) : (
                                <StatusText>Ошибка</StatusText>
                            )
                        }
                    </AdminOrderStatusContainer>

                    <TotalContainer>

                        <TotalContainer>
                            Итого:
                        </TotalContainer>
                        <TotalContainer>
                            {orderProps.total} грн
                        </TotalContainer>
                    </TotalContainer>
                    <AdminOrderControlButtons>
                        <CustomButton type='button' onClick={DecreaseStatus} adminUserProfileRed>ОКЛОНИТЬ</CustomButton>
                        <CustomButton type='button' onClick={IncreaseStatus} adminUserProfileGreen>Дальше</CustomButton>
                    </AdminOrderControlButtons>
                </AdminImageAndStatus>
                {
                    profileUpdateHidden ? (
                        <AdminDataContainer>
                            <AdminScrollData>
                                <UserData label={"Имя"} otherText={[orderProps.currentUser.displayName]}/>
                                <UserData label={"Электронная потча"} otherText={[orderProps.currentUser.email]}/>
                                <UserData
                                    label={"Телефон"}
                                    otherText={[orderProps.currentUser.phoneNumber]}
                                    phones/>
                                <UserData
                                    label={"Адресс для доставок"}
                                    otherText={[orderProps.currentUser.address]}
                                />
                                <UserData label={"Бонусные баллы"} otherText={[0]}/>
                            </AdminScrollData>
                            <CustomButton type='button' onClick={toggleUpdateHidden} userProfile>
                                Изменить
                            </CustomButton>
                        </AdminDataContainer>
                    ) : (
                        <DataContainer>
                            <FormContainer onSubmit={handleSubmit}>
                                <FormInput
                                    name='displayName'
                                    type='text'
                                    handleChange={handleChange}
                                    value={displayName}
                                    label='Имя'
                                    required
                                />
                                <FormInput
                                    name='email'
                                    type='email'
                                    value={email}
                                    handleChange={handleChange}
                                    label='Эл. почта'
                                    disabled
                                />
                                <FormInput
                                    name='phoneNumber'
                                    type='tel'
                                    value={phoneNumber}
                                    handleChange={handleChange}
                                    label='Телефон'
                                />
                                <FormInput
                                    name='address'
                                    autocomplete="street-address"
                                    type='text'
                                    value={address}
                                    handleChange={handleChange}
                                    label='Адрес'
                                />
                                <CustomButtonForm>
                                    <CustomButton type='submit' userProfile>Отмена</CustomButton>
                                    <CustomButton type='submit' adminUserProfileGreen>Готово</CustomButton>
                                </CustomButtonForm>
                            </FormContainer>
                        </DataContainer>
                    )}
                <AdminCartItemsContainer>
                    <AdminCartItems>
                        {
                            orderProps.cartItems ?
                                orderProps.cartItems.map(cartItem => (
                                        <OrderFixedItem key={cartItem.id} admin={true} cartItem={cartItem}/>
                                    )
                                ) : (
                                    <p>Ошибка</p>
                                )
                        }
                    </AdminCartItems>
                    <CustomButton type='button'>
                        Изменить
                    </CustomButton>
                </AdminCartItemsContainer>
            </UserInformation>

        </AdminOrderContainer>
    )
};

const mapStateToProps = createStructuredSelector({
    profileUpdateHidden: selectProfileUpdateHidden,
    orders: selectOrdersForPreview,
    allUsers: selectUsersForPreview
});

const mapDispatchToProps = dispatch => ({
    toggleUpdateHidden: () => dispatch(toggleUpdateHidden()),
    userUpdateStart: (displayName, email, phoneNumber, address) => dispatch(userUpdateStart({
        displayName,
        email,
        phoneNumber,
        address
    })),
    AdminUpdateOrderStatusStart: (userId, orderId, orderStatus) => dispatch(AdminUpdateOrderStatusStart({
        userId,
        orderId,
        orderStatus
    })),
    AdminGetOrdersStart: () => dispatch(AdminGetOrdersStart())
});

export default connect(mapStateToProps, mapDispatchToProps)(AdminNewOrders);