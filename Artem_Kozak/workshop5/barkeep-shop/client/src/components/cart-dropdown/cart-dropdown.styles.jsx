import styled from 'styled-components';
import CustomButton from '../custom-button/custom-button.component';

export const FullScreenDropdownContainer = styled.div`
  position: fixed;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  display: flex;
  z-index: 5;
`;

export const CloseCartDropdownContainer = styled.div`
  position: fixed;
  width: 100%;
  height: 100%;
  opacity: 0.15;
  background-color: black;
  z-index: 5;
`;

export const CartDropdownContainer = styled.div`
  margin: auto;
  width: 40%;
  height: 70%;
  display: flex;
  flex-direction: column;
  padding: 20px;
  border: 1px solid black;
  border-radius: 5px;
  background-color: white;
  z-index: 6;
  
  @media screen and (max-width: 800px) {
    border: 1px solid grey;
    background-color: #121212;
    width: 92%;
    height: 90%;
  }
`;

export const CartDropdownButton = styled(CustomButton)`
  margin-top: auto;
  height: 60px;
`;

export const EmptyMessageContainer = styled.span`
  font-size: 18px;
  margin: 50px auto;
`;

export const CloseCardTextContainer = styled.span`
  display: none;
  font-size: 14px;
  margin-left: auto;
  
  
  @media screen and (max-width: 800px) {
    display: unset;
    cursor: pointer;
    margin-bottom: 10px;
  }
`;

export const CartItemsContainer = styled.div`
  height: 100%;
  margin-bottom: 20px;
  
  flex-direction: column;
  overflow: scroll;
`;
