import styled, {css} from 'styled-components';

const buttonStyles = css`
  background-color: black;
  color: white;
  border: 1px solid black

  &:hover {
    background-color: white;
    color: black;
  }
  
  @media screen and (max-width: 800px) {
    background-color: black;
    color: white;
    border: 1px solid lightgrey;
  }
`;

const invertedButtonStyles = css`
  background-color: white;
  color: black;
  border: 1px solid black;

  &:hover {
    background-color: black;
    color: white;
  }
`;

const signAsInStyles = css`
  background-color: #4285f4;
  color: white;
  border: 1px solid #4285f4;

  &:hover {
    background-color: #357ae8;
  }
`;

const userProfileStyles = css`
  ${buttonStyles}
  margin-top: 40px;
`;

const adminUserProfileRedStyles = css`
  ${buttonStyles}
  background-color: rgb(255, 71, 0);
  margin-left: 5px;
`;

const adminUserProfileGreenStyles = css`
  ${buttonStyles}
  background-color: #00BF60;
  margin-top: 20px;
  margin-bottom: 10px;
  margin-left: 5px;
  font-size: 16px;
`;

const getButtonStyles = props => {
    if (props.isGoogleSignIn || props.isFacebookSignIn) {
        return signAsInStyles;
    }
    if (props.userProfile) {
        return userProfileStyles;
    }
    if (props.adminUserProfileRed) {
        return adminUserProfileRedStyles;
    }
    if (props.adminUserProfileGreen) {
        return adminUserProfileGreenStyles;
    }
    return props.inverted ? invertedButtonStyles : buttonStyles;
};

export const CustomButtonContainer = styled.button`
  width: auto;
  height: 50px;
  letter-spacing: 0.5px;
  line-height: 50px;
  padding: 0 35px 0 35px;
  font-size: 12px;
  text-transform: uppercase;
  font-family: 'Comfortaa', sans-serif;
  font-weight: bolder;
  cursor: pointer;
  display: flex;
  justify-content: center;
  border: 1px solid black;
  
  @media screen and (max-width: 800px){
    padding: 0 20px 0 20px;
  }
  
  ${getButtonStyles}
`;
