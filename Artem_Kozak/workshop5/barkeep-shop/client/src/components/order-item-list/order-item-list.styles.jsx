import styled from 'styled-components';

export const OrderItemListContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: start;
  margin-bottom: 10px;
  border-radius: 2px;
  border: 1px solid #A8ADAF;
`;

export const OrderHead = styled.div`
  width: 100%;
  padding: 10px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: end;
  border-bottom: 1px solid lightgrey;
  
  p {
    margin: 2px 0;
  }
`;

export const TotalPriceContainer = styled.div`
  width: 150px;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    font-size: 12px;
    line-height: 12px;
  }
`;

export const ArrayWithDetails = styled.div`
  width: 220px;
  display: flex;
  flex-direction: row;
  
  @media screen and (max-width: 800px) {
    width: 60px;
  }
`;

export const OrderStatusContainer = styled.div`
  width: 150px;
  display: flex;
  flex-direction: column;
  align-self: center;
  text-align: end;
`;

export const StatusText = styled.div`
  display: flex;
  flex-direction: column;
  border-radius: 15px;
  padding: 0 8px;
  font-size: 12px;
  line-height: 22px;
  height: auto;
  color: white;
  font-weight: 600;
  text-align: center;
  margin-left: auto;
  margin-right: 10px;
  
  &.green {
    background: #00BF60;
  }
  
  &.orange {
    background: #FFA000;
  }
  
  &.red {
    background: #ff3f00;
  }
  
  &.gray {
    background: #b4b4b4;
  }
  
  @media screen and (max-width: 800px) {
    font-size: 10px;
    line-height: 8px;
    padding: 5px 8px;
    
    &.gray {
      background: #7d7d7d;
    }
  }
`;

export const DateContainer = styled.div`
  margin-left: 10px; 
  display: flex;
  flex-direction: column;
  justify-content: center;
  
  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const Array = styled.div`
  width: 30px;
  height: 30px;
  fill: none;
  display: flex;
  flex-direction: column;
  border: 1px solid rgb(230, 230, 230);
  border-radius: 2px;
  transition: 0.5s ease;
  
  svg {
    transition: 0.5s ease;
    
    &.opened {
      transform: rotate(-180deg);
      transition: 0.5s ease;
    } 
  }
  
  @media screen and (max-width: 800px) {
    svg {
      path {
        fill: white !important;
      }
    }
  }
`;

export const OrderItemListItems = styled.div`
  width: 100%;
  padding: 10px;
  display: flex;
  flex-direction: row;
  align-items: start;
`;

export const OrderPreview = styled.div`
  width: 100%;
  padding: 0 10px;
  display: none;
  flex-direction: column;
  align-items: start;
  transition: 0.5s ease;
  
    
  &.opened {
    display: flex;
    transition: 0.5s ease;
  }
`;


export const OrderPreviewItem = styled.div`
  width: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: start;
  transition: 0.5s ease;
  
  p {
    margin: 0px 5px;
  }
`;

export const OrderItemContainer = styled.div`
  width: 80px;
  height: 80px;
  display: flex;
  margin-right: 15px;
  
  @media screen and (max-width: 800px) {  
    width: 50px;
    height: 50px;
  }
`;


export const ItemImage = styled.div` 
  width: 80px;
  height: 80px;
  background-size: cover;
  background-position: center;
  background-image: ${({imageUrl}) => `url(${imageUrl})`};
  display: flex;
  
  @media screen and (max-width: 800px) {  
    width: 50px;
    height: 50px;
  }
`;
