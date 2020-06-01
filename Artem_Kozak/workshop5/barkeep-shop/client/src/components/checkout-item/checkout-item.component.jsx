import React from 'react';
import {connect} from 'react-redux';

import {addItem, clearItemFromCart, removeItem} from '../../redux/cart/cart.actions';

import {
    CheckoutItemContainer,
    ImageContainer,
    PriceContainer,
    QuantityContainer,
    RemoveButtonContainer,
    TextContainer,
    TotalPriceContainer,
    TopLevelContainer,
    BottomLevelContainer,
    ButtonContainer
} from './checkout-item.styles';

const CheckoutItem = ({cartItem, clearItem, addItem, removeItem}) => {
    const {name, imageUrl, price, quantity} = cartItem;
    return (
        <CheckoutItemContainer>
            <TopLevelContainer >
                <ImageContainer>
                    <img src={imageUrl} alt='item'/>
                </ImageContainer>
                <TextContainer>{name}</TextContainer>
                <RemoveButtonContainer>
                    <ButtonContainer onClick={() => clearItem(cartItem)}>
                        &#10005;
                    </ButtonContainer>
                </RemoveButtonContainer>
            </TopLevelContainer>
            <BottomLevelContainer >
                <PriceContainer>{price}</PriceContainer>
                <QuantityContainer>
                    <div>
                        <button onClick={() => removeItem(cartItem)}>&#10094;</button>
                        <span>{quantity}</span>
                        <button onClick={() => addItem(cartItem)}>&#10095;</button>
                    </div>
                </QuantityContainer>
                <TotalPriceContainer>{price * quantity}</TotalPriceContainer>
            </BottomLevelContainer>
        </CheckoutItemContainer>
    );
};

const mapDispatchToProps = dispatch => ({
    clearItem: item => dispatch(clearItemFromCart(item)),
    addItem: item => dispatch(addItem(item)),
    removeItem: item => dispatch(removeItem(item))
});

export default connect(
    null,
    mapDispatchToProps
)(CheckoutItem);
