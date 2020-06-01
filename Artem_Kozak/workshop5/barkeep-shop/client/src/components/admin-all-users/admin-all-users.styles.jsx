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

export const ImageContainer = styled.div`
  width: 110px;
  height: 120px;
  border-radius: 100%;
  overflow: hidden;
  background-color: rgb(250, 250, 250);
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

