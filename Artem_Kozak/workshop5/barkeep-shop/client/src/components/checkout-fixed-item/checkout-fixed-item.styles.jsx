import styled, {css} from 'styled-components';

const textStyles = css`
  width: auto;
  font-size: 16px;
  margin: 0 10px;
  padding: 10px 0 0 0;
  
  @media screen and (max-width: 800px) { 
    padding-top: 5px; 
    font-size: 12px;
  }
  
  &.admin {
    font-size: 14px;
    padding-top: 5px;
  }
`;

export const HeaderContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: row;
`;

export const DescriptionContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
`;

export const BottomLevelContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: start;
  margin-top: 5px;
`;

export const CheckoutItemContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  min-height: 100px;
  border-top: 1px solid rgb(230, 230, 230);
  padding: 15px 0;
  font-size: 16px;
  align-items: center;
  
  &.admin:first-child {
    border: none;
  }
`;

export const ImageContainer = styled.div`
  width: 120px;
  height: 100px;
  border-radius: 2px;
  background-size: cover;
  background-position: center;
  background-image: ${({imageUrl}) => `url(${imageUrl})`};

  &.admin {
    width:80px;
    height: 70px;
  }

  img {
    border-radius: 2px;
    width: 100%;
    height: 100%;
  }
  
  @media screen and (max-width: 800px) {  
    width: 80px;
    height: 70px;
  }
`;

export const TextContainer = styled.span`
  width: 100%;
  font-size: 20px;
  padding-top: 10px;
  margin: 0 10px;
  
  &.admin {
    font-size: 16px;
    padding-top: 5px;
  }
  
  @media screen and (max-width: 800px) { 
    padding-top: 5px; 
    font-size: 15px;
  }
`;

export const PriceContainer = styled.span`
  ${textStyles}
`;

export const QuantityContainer = styled(TextContainer)`
  ${textStyles}
`;

export const TotalPriceContainer = styled.span`
  ${textStyles}
`;
