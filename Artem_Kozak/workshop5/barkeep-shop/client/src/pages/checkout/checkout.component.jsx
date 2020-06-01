import React from 'react';
import {connect} from 'react-redux';
import {Redirect} from "react-router-dom";
import {createStructuredSelector} from 'reselect';

import {
    CheckoutPageContainer,
    CheckoutBlock,
} from './checkout.styles';

import {
    selectCartItems, selectCartTotal,
} from '../../redux/cart/cart.selectors';

import CheckoutDataBlockContainerPage from "../../components/checkout-data/checkout-data.container";
import {TitleOfArticle} from "../terms-of-use/terms-of-use.styles";
import {
    CheckoutData,
    ItemsBlock,
    ItemsGroup,
    TotalContainer,
    UserDataBlock,
} from "../../components/checkout-data/checkout-data.styles";
import CheckoutItem from "../../components/checkout-item/checkout-item.component";
import {selectCurrentUser} from "../../redux/user/user.selectors";


const CheckoutPage = ({cartItems, total, currentUser}) => {
    return (
        <CheckoutPageContainer>
            {
                cartItems.length === 0 ? (
                    <Redirect to='/cart'/>
                ) : (
                    <CheckoutBlock>
                        <TitleOfArticle>Оформление заказа</TitleOfArticle>
                        <CheckoutData>
                            <UserDataBlock>
                                {
                                    currentUser ? (<CheckoutDataBlockContainerPage/>) : (
                                        <p>
                                            Для оформления заказа, войдите в личный кабинет, что бы нам было проще с
                                            Вами сязаться
                                        </p>)
                                }
                            </UserDataBlock>
                            <ItemsBlock>
                                <ItemsGroup>
                                    {cartItems.map(cartItem => (
                                        <CheckoutItem key={cartItem.id} cartItem={cartItem}/>
                                    ))}
                                </ItemsGroup>
                                <TotalContainer>Всего: {total} грн</TotalContainer>
                            </ItemsBlock>
                        </CheckoutData>
                    </CheckoutBlock>
                )
            }

        </CheckoutPageContainer>
    )
};

const mapStateToProps = createStructuredSelector({
    total: selectCartTotal,
    cartItems: selectCartItems,
    currentUser: selectCurrentUser
});

export default connect(mapStateToProps)(CheckoutPage);
