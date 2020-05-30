import React, {useState} from 'react';
import {connect} from 'react-redux';

import FormInput from '../form-input/form-input.component';
import CustomButton from '../custom-button/custom-button.component';

import {signUpStart} from '../../redux/user/user.actions';

import {SignUpContainer, SignUpTitle, SubDescriptionContainer, TermsLink} from './sign-up.styles';

const SignUp = ({signUpStart}) => {
    const [userCredentials, setUserCredentials] = useState({
        displayName: '',
        email: '',
        password: '',
        confirmPassword: ''
    });

    const {displayName, email, password, confirmPassword} = userCredentials;

    const handleSubmit = async event => {
        event.preventDefault();


        if (password !== confirmPassword) {
            alert("passwords don't match");
            return;
        }

        signUpStart({displayName, email, password});
    };

    const handleChange = event => {
        const {name, value} = event.target;

        setUserCredentials({...userCredentials, [name]: value});
    };

    return (
        <SignUpContainer>
            <SignUpTitle>Регистрация</SignUpTitle>
            <span>Присойденитесь используя почту и пароль</span>
            <form className='sign-up-form' onSubmit={handleSubmit}>
                <FormInput
                    type='text'
                    name='displayName'
                    value={displayName}
                    onChange={handleChange}
                    label='Ваше имя'
                    required
                />
                <FormInput
                    type='email'
                    name='email'
                    value={email}
                    onChange={handleChange}
                    label='Эл. почта'
                    required
                />
                <FormInput
                    type='password'
                    name='password'
                    value={password}
                    onChange={handleChange}
                    label='Придумайте пароль'
                    required
                />
                <FormInput
                    type='password'
                    name='confirmPassword'
                    value={confirmPassword}
                    onChange={handleChange}
                    label='Подтвердите пароль'
                    required
                />
                <SubDescriptionContainer>Регистрируясь, вы соглашаетесь с
                    <TermsLink to='/terms'> пользовательским соглашением</TermsLink>
                </SubDescriptionContainer>
                <CustomButton type='submit'>зарегистрироваться</CustomButton>
            </form>
        </SignUpContainer>
    );
};

const mapDispatchToProps = dispatch => ({
    signUpStart: userCredentials => dispatch(signUpStart(userCredentials))
});

export default connect(
    null,
    mapDispatchToProps
)(SignUp);
