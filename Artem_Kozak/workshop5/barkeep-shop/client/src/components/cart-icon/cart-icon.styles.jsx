import styled from 'styled-components';

import {ReactComponent as ShoppingIconSVG} from '../../assets/shopping-bag.svg';

const shoppingBag = ShoppingIconSVG;

export const CartContainer = styled.div`
  width: 45px;
  height: 45px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  
  @media screen and (max-width: 800px) {
    margin-right: 80px;
  }
`;

export const ShoppingIcon = styled(shoppingBag)`
  width: 24px;
  height: 24px;
  
  @media screen and (max-width: 800px) {
    g {
      path {
        fill: white !important;
      }
    }
  }
`;

export const ItemCountContainer = styled.span`
  position: absolute;
  font-size: 10px;
  font-weight: bold;
  bottom: 12px;
  
  @media screen and (max-width: 800px) {
    color: white;
  }
`;
