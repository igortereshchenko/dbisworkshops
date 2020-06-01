import styled from 'styled-components';

export const CheckoutPageContainer = styled.div`
  width: 55%;
  min-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 50px auto 0;

  button {
    margin-left: auto;
    margin-top: 50px;
  }
    
  @media screen and (max-width: 800px) {
    width: 100%;
    }
  }
  
  @media screen and (max-width: 800px) {
    padding: 15px;
    color: white;
  }
`;

export const CheckoutBlock = styled.div`
  width: 100%;
  min-height: 90vh;
`;

export const CheckoutHeaderContainer = styled.div`
  width: 100%;
  height: 1px;
  border-bottom: 1px solid darkgrey;
`;

export const TotalContainer = styled.div`
  margin-top: 30px;
  margin-left: auto;
  font-size: 36px;
  
  @media screen and (max-width: 800px) {
    font-size: 26px;
  }
`;

export const WarningContainer = styled.div`
  text-align: center;
  margin-top: 40px;
  font-size: 24px;
  color: red;
`;

export const EmptyMessage = styled.div`
  text-align: center;
  margin-top: 40px;
  font-size: 24px;
  color: grey;
  
  @media screen and (max-width: 800px) {
    font-size: 20px;
    color: rgb(120, 120, 120);
  }
`;
