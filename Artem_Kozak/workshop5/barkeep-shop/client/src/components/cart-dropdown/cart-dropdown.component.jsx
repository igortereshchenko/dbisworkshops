import React from 'react';
import {connect} from 'react-redux';
import {createStructuredSelector} from 'reselect';
import {withRouter} from 'react-router-dom';

// import CartItem from '../cart-item/cart-item.component';
import CheckoutItem from "../checkout-item/checkout-item.component";
import {selectCartItems} from '../../redux/cart/cart.selectors';
import {toggleCartHidden} from '../../redux/cart/cart.actions.js';

import {
    CartDropdownButton,
    CartDropdownContainer,
    CartItemsContainer,
    EmptyMessageContainer,
    FullScreenDropdownContainer,
    CloseCartDropdownContainer,
    CloseCardTextContainer
} from './cart-dropdown.styles';

const CartDropdown = ({cartItems, history, dispatch}) => (
    <FullScreenDropdownContainer>
        <CloseCartDropdownContainer onClick={() => {dispatch(toggleCartHidden())}}/>
        <CartDropdownContainer>
            <CloseCardTextContainer onClick={() => {dispatch(toggleCartHidden())}}>Закрыть</CloseCardTextContainer>
            <CartItemsContainer>
                {cartItems.length ? (
                    cartItems.map(cartItem => (
                        <CheckoutItem key={cartItem.id} cartItem={cartItem}/>
                    ))
                ) : (
                    <EmptyMessageContainer>Корзина пустая</EmptyMessageContainer>
                )}
            </CartItemsContainer>
            <CartDropdownButton
                onClick={() => {
                    history.push('/checkout');
                    dispatch(toggleCartHidden());
                }}
            >
                Оформить Заказ
            </CartDropdownButton>
        </CartDropdownContainer>
    </FullScreenDropdownContainer>
);

const mapStateToProps = createStructuredSelector({
    cartItems: selectCartItems
});

export default withRouter(connect(mapStateToProps)(CartDropdown));
