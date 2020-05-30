import React from 'react';
import {Redirect, Route, Switch} from 'react-router-dom';
import {connect} from 'react-redux';
import {createStructuredSelector} from 'reselect';

import {GlobalStyle} from './global.styles';

import HomePage from './pages/homepage/homepage.component';
import ShopPage from './pages/shop/shop.component';
import SignInAndSignUpPage from './pages/sign-in-and-sign-up/sign-in-and-sign-up.component';
import CartPage from './pages/cart/checkout.component';
import CheckoutPage from "./pages/checkout/checkout.component";
import TermOfUsePage from "./pages/terms-of-use/terms-of-use.component";
import ProfilePage from "./pages/profile/profile.component";

import Header from './components/header/header.component';
import MobileHeader from "./components/mobile-header/mobile-header.component";

import {selectCurrentUser} from './redux/user/user.selectors';
import {checkUserSession} from './redux/user/user.actions';
import AdminPage from "./pages/admin/admin.component";

class App extends React.Component {
    unsubscribeFromAuth = null;

    componentDidMount() {
        const {checkUserSession} = this.props;
        checkUserSession();
    }

    componentWillUnmount() {
        this.unsubscribeFromAuth();
    }

    render() {
        return (
            <div>
                <GlobalStyle/>
                <Header/>
                <MobileHeader/>
                <Switch>
                    <Route exact path='/' component={HomePage}/>
                    <Route path='/administrator_page_for_user_orders_and_other' render={() =>
                        this.props.currentUser && this.props.currentUser.uid === 'JOZY7zzZx9fsgna5BBGWuIIJHzi2' ? (
                            <AdminPage/>
                        ) : (
                            null
                            // <Redirect to='/'/>
                        )}
                    />
                    <Route path='/profile' component={ProfilePage}/>
                    <Route path='/shop' component={ShopPage}/>
                    <Route exact path='/cart' component={CartPage}/>
                    <Route exact path='/checkout' component={CheckoutPage}/>
                    <Route exact path='/terms' component={TermOfUsePage}/>
                    <Route
                        exact
                        path='/signin'
                        render={() =>
                            this.props.currentUser ? (
                                <Redirect to='/'/>
                            ) : (
                                <SignInAndSignUpPage/>
                            )
                        }
                    />
                </Switch>
            </div>
        );
    }
}

const mapStateToProps = createStructuredSelector({
    currentUser: selectCurrentUser
});

const mapDispatchToProps = dispatch => ({
    checkUserSession: () => dispatch(checkUserSession())
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(App);
