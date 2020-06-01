import React from 'react';
import {createStructuredSelector} from "reselect";
import {connect} from "react-redux";

import {selectOrderHidden} from "../../redux/orders/orders.selectors";
import {setOrderHidden} from "../../redux/orders/orders.actions";
import OrderFixedItem from "../checkout-fixed-item/checkout-fixed-item.component";

import {
    OrderItemListContainer,
    OrderHead,
    ArrayWithDetails,
    TotalPriceContainer,
    OrderItemListItems,
    OrderStatusContainer,
    DateContainer,
    ItemImage,
    StatusText,
    Array,
    OrderPreview,
    OrderItemContainer,
} from './order-item-list.styles'

const options = {
    weekday: 'short',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    timezone: 'UTC'
};

const OrderItemList = ({orderId, cartItems, createdAt, orderStatus, total, setOrderHidden, orderIsOpen}) => {
    const quantity = cartItems.reduce((accumulatedQuantity, cartItem) =>
        accumulatedQuantity + cartItem.quantity, 0);


    const handleClick = (orderIsOpen, orderId) => {
        orderIsOpen === orderId ? setOrderHidden(null) : setOrderHidden(orderId);
    }

    const declOfNum = (number, titles) => {
        const cases = [2, 0, 1, 1, 1, 2];
        return titles[(number % 100 > 4 && number % 100 < 20) ? 2 : cases[(number % 10 < 5) ? number % 10 : 5]];
    }


    return (
        <OrderItemListContainer>
            <OrderHead>
                <ArrayWithDetails>
                    <Array onClick={() => handleClick(orderIsOpen, orderId)}>
                        <svg className={orderIsOpen === orderId ? 'opened' : ''}
                             width="30" height="30"
                             viewBox="0 0 24 24" fill="none"
                             xmlns="http://www.w3.org/2000/svg">
                            <path d="M7.41 8.59L12 13.17L16.59 8.59L18 10L12 16L6 10L7.41 8.59Z" fill="#263238"/>
                        </svg>
                    </Array>
                    <DateContainer>
                        <p>{createdAt.toDate().toLocaleString("UA", options)}</p>
                    </DateContainer>
                </ArrayWithDetails>
                <TotalPriceContainer>
                    <p>{quantity} {declOfNum(quantity, ['товар', 'товара', 'товаров'])}</p>
                    <p>на сумму {total} грн</p>
                </TotalPriceContainer>
                <OrderStatusContainer>
                    {
                        orderStatus === -1 ? (
                            <StatusText className={'orange'}>Отменен</StatusText>
                        ) : orderStatus === 0 ? (
                            <StatusText className={'gray'}>Новый заказ</StatusText>
                        ) : orderStatus === 1 ? (
                            <StatusText className={'gray'}>Обработан</StatusText>
                        ) : orderStatus === 2 ? (
                            <StatusText className={'gray'}>Доставляется</StatusText>
                        ) : orderStatus >= 3 ? (
                            <StatusText className={'green'}>Выполнен</StatusText>
                        ) : (
                            <StatusText>Ошибка</StatusText>
                        )
                    }
                </OrderStatusContainer>
            </OrderHead>
            <OrderItemListItems>
                {cartItems.map(({id, imageUrl}) =>
                    <OrderItemContainer key={id}>
                        <ItemImage imageUrl={imageUrl}/>
                    </OrderItemContainer>
                )}
            </OrderItemListItems>
            <OrderPreview className={orderIsOpen === orderId ? 'opened' : ''}>
                {cartItems.map((cartItem) =>
                    <OrderFixedItem key={cartItem.id} cartItem={cartItem}/>
                )}
            </OrderPreview>
        </OrderItemListContainer>)
};

const mapStateToProps = createStructuredSelector({
    orderIsOpen: selectOrderHidden,
});

const mapDispatchToProps = dispatch => ({
    setOrderHidden: orderId => dispatch(setOrderHidden(orderId))
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(OrderItemList);