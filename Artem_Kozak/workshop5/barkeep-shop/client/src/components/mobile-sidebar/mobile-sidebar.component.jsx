import React from 'react';
import {connect} from 'react-redux';
import {createStructuredSelector} from 'reselect';
import {selectCurrentUser} from '../../redux/user/user.selectors';
import {signOutStart} from '../../redux/user/user.actions';


import {
    CheckoutInput,
    FullScreenMenuContainer,
    ListItem,
    MenuButtonContainer,
    MenuItem,
    MenuToggle,
    MenuToggleSpan,
    Nav,
    OptionLink
} from "./mobile-sidebar.styles";
import {selectSidebarHidden} from "../../redux/sidebar/sidebar.selectors";
import {toggleSidebarHidden} from "../../redux/sidebar/sidebar.actions";

const MobileMenuFixedButton = ({sidebarHidden, currentUser, toggleSidebarHidden, signOutStart}) => (
    <MenuButtonContainer className='button-container'>
        <Nav role="navigation">
            <MenuToggle id="menuToggle">
                {!sidebarHidden ? <FullScreenMenuContainer onClick={toggleSidebarHidden}/> : null}
                <CheckoutInput onChange={toggleSidebarHidden} checked={!sidebarHidden} type="checkbox"/>
                <MenuToggleSpan/>
                <MenuToggleSpan/>
                <MenuToggleSpan/>
                <MenuItem id='menu'>
                    {currentUser ? (
                        <ListItem onClick={toggleSidebarHidden}>
                            <OptionLink to="/profile">
                                <p>Здравствуйте,</p>
                                <p>{currentUser.displayName}</p>
                            </OptionLink>
                        </ListItem>
                    ) : (
                        <ListItem onClick={toggleSidebarHidden}>
                            <OptionLink to='/signin'>
                                <p>Войдите</p>
                                <p>в личный кабинет</p>
                            </OptionLink>
                        </ListItem>
                    )}
                    <ListItem onClick={toggleSidebarHidden}><OptionLink to="/">Домой</OptionLink></ListItem>
                    <ListItem onClick={toggleSidebarHidden}><OptionLink to="/shop">Магазин</OptionLink></ListItem>
                    <ListItem onClick={toggleSidebarHidden}><OptionLink to="/checkout">Корзина</OptionLink></ListItem>
                    <ListItem onClick={toggleSidebarHidden}><OptionLink to="/shop">О нас</OptionLink></ListItem>
                    {currentUser ? (
                        <ListItem onClick={toggleSidebarHidden}>
                            <OptionLink className='userExit' as='div' onClick={signOutStart}>
                                Выйти
                            </OptionLink>
                        </ListItem>
                    ) : null}
                </MenuItem>
            </MenuToggle>
        </Nav>
    </MenuButtonContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
    sidebarHidden: selectSidebarHidden,
});

const mapDispatchToProps = dispatch => ({
    signOutStart: () => dispatch(signOutStart()),
    toggleSidebarHidden: () => dispatch(toggleSidebarHidden())
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(MobileMenuFixedButton);
