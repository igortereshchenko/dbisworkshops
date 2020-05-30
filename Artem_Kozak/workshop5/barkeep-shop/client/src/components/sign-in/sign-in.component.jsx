import React, {useState} from 'react';
import {connect} from 'react-redux';

import FormInput from '../form-input/form-input.component';
import CustomButton from '../custom-button/custom-button.component';

import {emailSignInStart, googleSignInStart, facebookSignInStart} from '../../redux/user/user.actions';

import {
    ButtonsBarContainer,
    SignInContainer,
    SignInTitle,
    OrLineContainer,
    SingInAsContainer
} from './sign-in.styles';

const SignIn = ({emailSignInStart, googleSignInStart, facebookSignInStart}) => {
    const [userCredentials, setCredentials] = useState({email: '', password: ''});

    const {email, password} = userCredentials;

    const handleSubmit = async event => {
        event.preventDefault();

        emailSignInStart(email, password);
    };

    const handleChange = event => {
        const {value, name} = event.target;

        setCredentials({...userCredentials, [name]: value});
    };

    return (
        <SignInContainer>
            <SignInTitle>Вход</SignInTitle>
            <span>Войти в аккаунт используя почту и пароль</span>
            <form onSubmit={handleSubmit}>
                <FormInput
                    name='email'
                    type='email'
                    handleChange={handleChange}
                    value={email}
                    label='Эл. почта'
                    required
                />
                <FormInput
                    name='password'
                    type='password'
                    value={password}
                    handleChange={handleChange}
                    label='Пароль'
                    required
                />
                <CustomButton type='submit'> Войти </CustomButton>
            </form>
            <OrLineContainer>
                <hr />
                <span>Или</span>
                <hr />
            </OrLineContainer>
            <SingInAsContainer>
                <span>Войти как пользователь</span>
            </SingInAsContainer>
            <ButtonsBarContainer>
                <CustomButton
                    type='button'
                    onClick={googleSignInStart}
                    isGoogleSignIn
                >
                    Google
                </CustomButton>
                <CustomButton
                    type='button'
                    onClick={facebookSignInStart}
                    isFacebookSignIn
                >
                    Facebook
                </CustomButton>
            </ButtonsBarContainer>
        </SignInContainer>
    );
};

const mapDispatchToProps = dispatch => ({
    googleSignInStart: () => dispatch(googleSignInStart()),
    facebookSignInStart: () => dispatch(facebookSignInStart()),
    emailSignInStart: (email, password) =>
        dispatch(emailSignInStart({email, password}))
});

export default connect(
    null,
    mapDispatchToProps
)(SignIn);
