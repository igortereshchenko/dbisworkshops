import styled from 'styled-components';

export const OrderItemContainer = styled.div`
  width: 100px;
  height: 100px;
  display: flex;
  margin-right: 15px;
  
  @media screen and (max-width: 800px) {  
    width: 50px;
    height: 50px;
  }
`;


export const ItemImage = styled.div` 
  width: 100px;
  height: 100px;
  background-size: cover;
  background-position: center;
  background-image: ${({imageUrl}) => `url(${imageUrl})`};
  display: flex;
  
  @media screen and (max-width: 800px) {  
    width: 50px;
    height: 50px;
  }
`;
