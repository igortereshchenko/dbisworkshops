import React, {useState} from 'react';
import {createStructuredSelector} from "reselect";

import {
    CheckoutDataContainer,
    TotalContainer,
    CheckoutData,
    CheckoutUserTitle,
    CheckoutContactData,
    ItemsBlock,
    CheckoutFormContainer,
    ItemsGroup,
    UserDataBlock
} from './checkout-data.styles';

import FormInputForData from "../form-input-for-data/form-input-for-data.component";
import CustomButton from "../custom-button/custom-button.component";

import {userUpdateStart} from "../../redux/user/user.actions";
import {createNewOrderStart} from "../../redux/cart/cart.actions";
import {connect} from "react-redux";
import {selectCartItems, selectCartItemsCount, selectCartTotal} from "../../redux/cart/cart.selectors";
import {selectCurrentUser} from "../../redux/user/user.selectors";


const CheckoutDataBlock = ({cartItems, total, currentUser, itemsCount, userUpdateStart, createNewOrderStart}) => {
    const [userCredentials, setCredentials] = useState({
        uid: `${currentUser.uid}`,
        displayName: `${currentUser.displayName}`,
        email: `${currentUser.email}`,
        phoneNumber: `${currentUser.phoneNumber == null ? '+380' : currentUser.phoneNumber}`,
        address: `${currentUser.address == null ? '' : currentUser.address}`,
    });

    const {uid, displayName, email, phoneNumber, address} = userCredentials;

    const handleSubmit = async event => {
        event.preventDefault();
        userUpdateStart(displayName, email, phoneNumber, address);
        const orderUserData = {uid, displayName, email, phoneNumber, address};
        createNewOrderStart(orderUserData, cartItems, total, itemsCount);
    };

    const handleChange = event => {
        const {value, name} = event.target;

        setCredentials({...userCredentials, [name]: value});
    };

    return (
        <CheckoutDataContainer>
            <UserDataBlock>
                <CheckoutUserTitle>
                    Контактные данные
                </CheckoutUserTitle>
                <CheckoutContactData>
                    <CheckoutFormContainer>
                        <FormInputForData
                            name='displayName'
                            type='text'
                            handleChange={handleChange}
                            value={displayName}
                            label='Имя и фамилия'
                            required
                        />
                        <FormInputForData
                            name='email'
                            type='email'
                            handleChange={handleChange}
                            value={email}
                            label='Электронная почта'
                            disabled
                        />
                        <FormInputForData
                            name='phoneNumber'
                            type='tel'
                            handleChange={handleChange}
                            value={phoneNumber}
                            label='Телефон'
                            required
                        />
                        <FormInputForData
                            name='address'
                            type='text'
                            handleChange={handleChange}
                            value={address}
                            label='Адрес получателя'
                            required
                        />
                        <CustomButton onClick={handleSubmit}>Заказ подтверждаю</CustomButton>
                    </CheckoutFormContainer>
                </CheckoutContactData>
            </UserDataBlock>
        </CheckoutDataContainer>
    )
};

const mapStateToProps = createStructuredSelector({
    cartItems: selectCartItems,
    total: selectCartTotal,
    currentUser: selectCurrentUser,
    itemsCount: selectCartItemsCount
});

const mapDispatchToProps = dispatch => ({
    userUpdateStart: (displayName, email, phoneNumber, address) => dispatch(userUpdateStart({
        displayName,
        email,
        phoneNumber,
        address
    })),
    createNewOrderStart: (orderUserData, cartItems, total) => dispatch(createNewOrderStart({
        orderUserData, cartItems, total
    }))
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(CheckoutDataBlock);
