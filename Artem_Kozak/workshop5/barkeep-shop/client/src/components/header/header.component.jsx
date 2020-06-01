import React from 'react';
import {connect} from 'react-redux';
import {createStructuredSelector} from 'reselect';
import CartIcon from '../cart-icon/cart-icon.component';
import CartDropdown from '../cart-dropdown/cart-dropdown.component';
import {selectCartHidden} from '../../redux/cart/cart.selectors';
import {selectCurrentUser} from '../../redux/user/user.selectors';
import {signOutStart} from '../../redux/user/user.actions';

import {ReactComponent as Logo} from '../../assets/crown.svg';

import {
    CurrentUserContainer,
    SubMenuContainer,
    HeaderContainer,
    LogoContainer,
    OptionLink,
    OptionsContainer,
    OptionsTextContainer,
    MenuItemContainer,
    MenubarItemDropdown
} from './header.styles';

const Header = ({currentUser, hidden, signOutStart}) => (
    <HeaderContainer>
        <LogoContainer to='/'>
            <Logo className='logo'/>
        </LogoContainer>
        <OptionsContainer>
            <OptionsTextContainer>
                <OptionLink to='/shop'>Магазин</OptionLink>
                <OptionLink to='/shop'>О нас</OptionLink>
                {currentUser ? (
                    <MenuItemContainer>
                        <CurrentUserContainer>
                            Здравствуйте, {currentUser.displayName}
                        </CurrentUserContainer>
                        <SubMenuContainer>{
                            currentUser.uid === 'JOZY7zzZx9fsgna5BBGWuIIJHzi2' ? (
                                <MenubarItemDropdown to='/administrator_page_for_user_orders_and_other/'>Я
                                    администратор</MenubarItemDropdown>

                            ) : null
                        }
                            <MenubarItemDropdown to='/profile/personal-information/'>Личные данные</MenubarItemDropdown>
                            <MenubarItemDropdown to='/checkout'>Корзина</MenubarItemDropdown>
                            <MenubarItemDropdown as='div' onClick={signOutStart}>Выйти</MenubarItemDropdown>
                        </SubMenuContainer>
                    </MenuItemContainer>
                ) : (
                    <OptionLink to='/signin'>Войдите в личный кабинет</OptionLink>
                )}
            </OptionsTextContainer>
            <CartIcon/>
        </OptionsContainer>
        {hidden ? null : <CartDropdown/>}
    </HeaderContainer>
);

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser,
    hidden: selectCartHidden
});

const mapDispatchToProps = dispatch => ({
    signOutStart: () => dispatch(signOutStart())
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Header);
