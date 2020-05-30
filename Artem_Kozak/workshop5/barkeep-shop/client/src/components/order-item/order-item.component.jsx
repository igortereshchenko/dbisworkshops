import React from 'react';

import {
    OrderItemContainer,
    ItemImage,
} from './order-item.styles'


const OrderItem = ({imageUrl}) => (
    <OrderItemContainer>
        <ItemImage imageUrl={imageUrl}/>
    </OrderItemContainer>
);

export default OrderItem;