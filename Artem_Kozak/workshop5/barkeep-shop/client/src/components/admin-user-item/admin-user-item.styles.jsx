import styled from 'styled-components';

export const AdminAllUsersContainer = styled.div`
  width: 1080px;
  min-height: 610px;
  padding: 20px 40px;
`;

export const AdminHeaderContainer = styled.div`
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 40px;
`;

export const TitleContainer = styled.h1`
  font-size: 28px;
  margin: 0;
  margin-bottom: 20px;
`;

export const AdminUserBlock = styled.div`
  width: 1000px;
  padding: 10px;
  height: 170px;
  display: flex;
  border-radius: 2px;
  margin-bottom: 40px;
  flex-direction: row;
  background-color: rgb(250, 250, 250); 
  box-shadow: 0px 2px 8px 0px rgba(0,0,0,0.3);
`;

export const AdminUserHead = styled.div`
  width: 130px;
  height: 130px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 100%;
  box-shadow: 0px 2px 12px 0px rgba(0,0,0,0.3);
  
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
`;

export const ImageContainer = styled.div`
  width: 110px;
  height: 120px;
  border-radius: 100%;
  overflow: hidden;
  background-color: rgb(250, 250, 250);
`;

export const AdminUserBody = styled.div`
  width: 610px;
  margin: 0 20px;
  padding: 10px;
  height: 150px;
  overflow: scroll;
`;

export const AdminUserDataText = styled.div`
  width: 600px;
  padding: 10px;
  display: grid;
  grid-template-columns: 13% 82%;
  grid-gap: 10px;
  line-height: 12px;
  
  
  p {
    margin: auto 0 0 0;
    
    &:last-child {
      font-weight: bold;
      font-size: 16px;
    } 
  }
`;

export const AdminUserFooter = styled.div`
  width: 200px;
  padding: 10px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

export const AdminUserInformation = styled.div`
  width: 120px;
  height: 120px;
  border-radius: 100%;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 70px;
  transition: 0.2s ease;
  
  &:hover {
    box-shadow: 0px 2px 12px 0px rgba(0,0,0,0.3);
    background-color: white;
    cursor: pointer;
    transition: 0.3s ease;
  }
`;

export const AdminCustomButtonContainer = styled.button`
  width: auto;
  height: 50px;
  letter-spacing: 0.5px;
  line-height: 50px;
  padding: 0 35px 0 35px;
  font-size: 12px;
  text-transform: uppercase;
  font-family: 'Comfortaa', sans-serif;
  font-weight: bolder;
  cursor: pointer;
  display: flex;
  justify-content: center;
  border: 1px solid black;
  background-color: white;
  border-radius: 15px;
  
  @media screen and (max-width: 800px){
    padding: 0 20px 0 20px;
  }
`;

