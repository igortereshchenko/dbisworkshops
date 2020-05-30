import styled from 'styled-components';

export const AdminNewOrdersContainer = styled.div`
  width: 1200px;
  min-height: 610px;
  padding: 20px 40px;
`;

export const AdminOrderContainer = styled.div`
  width: 100%;
  padding: 10px;
  margin-bottom: 60px;
  border-radius: 3px;
  box-shadow: 0px 4px 10px 0px rgba(0,0,0,0.2);
`;

export const UserInformation = styled.div`
  width: 100%;
  height: 550px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
`;

export const ImageContainer = styled.div`
  width: 160px;
  height: 160px;
  margin-left: 15px;
  border-radius: 100%;
  overflow: hidden;
  -webkit-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
`;

export const DefaultBackgroundImage = styled.div`
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-image: url(https://i.ibb.co/hZ57trj/default-avatar.png);
  
  @media screen and (max-width: 800px) {
    filter: invert(0.9);
  }
`;

export const TitleContainer = styled.h1`
  font-size: 28px;
  margin: 0;
  margin-bottom: 20px;
`;

export const AdminDataContainer = styled.div`
  font-size: 16px;
  height: 550px;
  padding: 10px;
  width: 420px;
  display: flex; 
  flex-direction: column;
  justify-content: space-between;
  border-radius: 5px;
  -webkit-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  
  button {
    margin: 0;
  }
`;

export const AdminImageAndStatus = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  font-size: 16px;
`;

export const AdminOrderControlButtons = styled.div`
  display: flex;
  flex-direction: column;
  height: auto;
  justify-content: end;
  
  button {
    width: 100%;
  }
`;

export const AdminScrollData = styled.div`
  padding: 0;
  margin: 0;
  width: 100%;
  display: flex; 
  flex-direction: column;
  max-height: 460px;
  overflow: scroll;
`;

export const FormContainer = styled.form`
  width: 100%;
  height: 100%;
  
  @media screen and (max-width: 800px) {
    width: 100%;
  }
`;

export const CustomButtonForm = styled.form`
  width: 100%;
  display: flex; 
  flex-direction: row;
  
  button {
    width: 100%;
    padding: 0;
    margin: 0 10px;
  }
`;

export const DataContainer = styled.div`
  font-size: 16px;
  height: 550px;
  padding: 10px;
  width: 420px;
  display: flex; 
  flex-direction: column;
  justify-content: space-between;
  border-radius: 5px;
  -webkit-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
`;

export const AdminCartItemsContainer = styled.div`
  width: 420px;
  height: 550px;
  padding: 10px;
  display: flex; 
  flex-direction: column;
  justify-content: space-between;
  border-radius: 4px;
  -webkit-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  box-shadow: 0px 5px 10px 0px rgba(0,0,0,0.2);
  
  button {
  
  }
`;

export const AdminCartItems = styled.div`
  padding: 0;
  margin: 0;
  width: 100%;
  display: flex; 
  flex-direction: column;
  max-height: 460px;
  overflow: scroll;
`;

export const AdminOrderStatusContainer = styled.div`
  width: 150px;
  align-self: start;
  padding-bottom: 20px;
`;

export const StatusText = styled.div`
  display: flex;
  flex-direction: column;
  border-radius: 15px;
  padding: 0 8px;
  font-size: 14px;
  line-height: 24px;
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