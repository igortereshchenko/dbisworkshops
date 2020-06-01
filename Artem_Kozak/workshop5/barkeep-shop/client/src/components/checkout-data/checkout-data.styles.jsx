import styled from "styled-components";

export const CheckoutDataContainer = styled.div`
  width: 100%;
  min-height: 55vh;
  display: flex;
  flex-direction: row;
`;

export const CheckoutData = styled.div`
  width: 100%;
  display: flex;
  flex-direction: row;
  
  @media screen and (max-width: 800px) {
    flex-direction: column;
  }
`;

export const ItemsBlock = styled.div`
  width: 80%;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    order: 1;
    width: 95%;
    align-self: center;
  }
`;

export const CheckoutFormContainer = styled.form`
`;

export const ItemsGroup = styled.div`
  width: 100%;
  padding: 10px;
  max-height: 440px;
  overflow: scroll;
  border-radius: 5px;
  -webkit-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  
  @media screen and (max-width: 800px) {
    background-color: rgb(12, 12, 12);
     max-height: 62vh;
  }
`;

export const UserDataBlock = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    order: 2;
    width: 95%;
    align-self: center;
  }
`;

export const TotalContainer = styled.div`
  margin-top: 30px;
  margin-left: auto;
  font-size: 22px;
  
  @media screen and (max-width: 800px) {
    font-size: 18px;
  }
`;

export const CheckoutUserTitle = styled.div`
  margin-top: 20px;
  margin-left: 20px;
  font-size: 22px;
  
  @media screen and (max-width: 800px) {
    font-size: 18px;
    margin-left: 0;
    margin-top: 40px;
  }
`;

export const CheckoutContactData = styled.div`
  margin: 0px 20px;
  font-size: 22px;
  padding: 20px 40px;
  
  @media screen and (max-width: 800px) {
    margin: 0;
    font-size: 18px;
    padding: 0;
  }
`;