import React from 'react';
import {connect} from 'react-redux';

import {
    CheckoutItemContainer,
    ImageContainer,
    PriceContainer,
    QuantityContainer,
    DescriptionContainer,
    TextContainer,
    TotalPriceContainer,
    HeaderContainer,
    BottomLevelContainer,
} from './checkout-fixed-item.styles';

const OrderFixedItem = ({cartItem, admin}) => {
    const {name, imageUrl, price, quantity} = cartItem;
    return (
        <CheckoutItemContainer className={admin ? 'admin' : ''}>
            <HeaderContainer className={admin ? 'admin' : ''}>
                <ImageContainer imageUrl={imageUrl} alt='item' className={admin ? 'admin' : ''}/>
                <DescriptionContainer className={admin ? 'admin' : ''}>
                    <TextContainer className={admin ? 'admin' : ''}>{name}</TextContainer>
                    <BottomLevelContainer className={admin ? 'admin' : ''}>
                        <PriceContainer className={admin ? 'admin' : ''}>{price} грн</PriceContainer>
                        <QuantityContainer className={admin ? 'admin' : ''}>х {quantity} шт.</QuantityContainer>
                        <TotalPriceContainer
                            className={admin ? 'admin' : ''}>Итого {price * quantity} грн</TotalPriceContainer>
                    </BottomLevelContainer>
                </DescriptionContainer>
            </HeaderContainer>
        </CheckoutItemContainer>
    );
};

const mapDispatchToProps = dispatch => ({});

export default connect(
    null,
    mapDispatchToProps
)(OrderFixedItem);
