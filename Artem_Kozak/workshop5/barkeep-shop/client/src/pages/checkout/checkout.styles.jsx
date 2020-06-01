import styled from 'styled-components';

export const CheckoutPageContainer = styled.div`
  width: 700px;
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
    padding: 15px;
    color: white;
    margin: 0;
    
    button {
      width: 100%;
      margin-left: auto;
      margin-top: 50px;
    }
  }
  
  @media screen and (min-width: 1200px) {
    width: 60vw;
  }
`;

export const CheckoutBlock = styled.div`
  width: 100%;
  min-height: 90vh;
`;