import React from 'react';
import {connect} from 'react-redux';
import {createStructuredSelector} from 'reselect';

import StripeCheckoutButton from '../../components/stripe-button/stripe-button.component';
import CheckoutItem from '../../components/checkout-item/checkout-item.component';

import {
    selectCartItems,
    selectCartTotal
} from '../../redux/cart/cart.selectors';

import {
    CheckoutPageContainer,
    CheckoutHeaderContainer,
    TotalContainer,
    WarningContainer,
    CheckoutBlock,
    EmptyMessage
} from './checkout.styles';

const CartPage = ({cartItems, total}) => (
    <CheckoutPageContainer>
        {
            cartItems.length === 0 ? (
                <CheckoutBlock>
                    <EmptyMessage>
                        Корзина пуста
                        <br/>
                        <br/>
                        Но это никогда не поздно исправить :)
                    </EmptyMessage>
                </CheckoutBlock>
            ) : (
                <CheckoutBlock>
                    <CheckoutHeaderContainer/>
                    {cartItems.map(cartItem => (
                        <CheckoutItem key={cartItem.id} cartItem={cartItem}/>
                    ))}
                    <TotalContainer>Всего: {total} грн</TotalContainer>
                    <WarningContainer>
                        *Для покупки используйте следующие реквизиты:*
                        <br/>
                        4242 4242 4242 4242 - Exp: 01/23 - CVV: 123
                    </WarningContainer>
                    <StripeCheckoutButton price={total}/>
                </CheckoutBlock>
            )
        }

    </CheckoutPageContainer>
);

const mapStateToProps = createStructuredSelector({
    cartItems: selectCartItems,
    total: selectCartTotal
});

export default connect(mapStateToProps)(CartPage);
