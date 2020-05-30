import styled from 'styled-components';

export const TopLevelContainer = styled.div`
  width: 100%;
  display: flex;
`;

export const BottomLevelContainer = styled.div`
  width: 100%;
  display: flex;
  margin-top: 15px;
`;

export const CheckoutItemContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  min-height: 100px;
  border-bottom: 1px solid darkgrey;
  padding: 15px 0;
  font-size: 20px;
  align-items: center;
`;

export const ImageContainer = styled.div`
  width: 20%;
  padding-right: 15px;

  img {
    width: 100%;
    height: 100%;
  }
`;

export const TextContainer = styled.span`
  width: 70%;
  }
`;

export const RemoveButtonContainer = styled.div`
  cursor: pointer;
  width: 10%;
`;

export const ButtonContainer = styled.div`
  cursor: pointer;
  margin-left: auto;
  width: 30px;
  height: 30px;
  text-align: center;
  
  @media screen and (max-width: 800px) {
    color: white;
  }
`;

export const PriceContainer = styled.span`
  width: 35%;
`;

export const QuantityContainer = styled(TextContainer)`
  display: flex;
  width: 30%;

  span {
    margin: 0 10px;
  }

  div {
    display: flex;
    margin-left: auto;
    margin-right: auto;
    
    button {
      margin: 0;
      background-color: white;
      color: black;
      border: 1px solid #e7e7e7; /* Grey */
    }
  }
}
`;

export const TotalPriceContainer = styled.span`
  width: 35%;
  text-align: right;
}
`;
