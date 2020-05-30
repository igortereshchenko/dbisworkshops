import React from 'react';
import {connect} from "react-redux";
import {createStructuredSelector} from "reselect";

import CartIcon from '../cart-icon/cart-icon.component';
import CartDropdown from "../cart-dropdown/cart-dropdown.component";
import MobileMenuFixedButton from "../mobile-sidebar/mobile-sidebar.component";

import {selectCartHidden} from "../../redux/cart/cart.selectors";

import {
    HeaderContainer,
    LogoContainer,
} from './mobile-header.styles';


const MobileHeader = ({hidden}) => (
    <HeaderContainer>
        <LogoContainer to='/'>
            <p>Barkeep Shop</p>
        </LogoContainer>
        <CartIcon/>
        <MobileMenuFixedButton/>
        {hidden ? null : <CartDropdown/>}
    </HeaderContainer>
);

const mapStateToProps = createStructuredSelector({
    hidden: selectCartHidden,
});

export default connect(
    mapStateToProps,
    null
)(MobileHeader);
