import styled from 'styled-components';

export const PersonalInformationContainer = styled.div`
  padding: 30px;
  display: flex;
  flex-direction: column;
  width: 700px;
  
  @media screen and (max-width: 800px) {
    width: 100%;
    font-size: 12px;
  }
`;

export const HeadContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: baseline;
  padding: 20px 20px;
`;

export const DataContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: baseline;
`;

export const ImageContainer = styled.div`
  width: 130px;
  height: 130px;
  border-radius: 100%;
  overflow: hidden;
`;

export const FormContainer = styled.form`
  width: 80%;
  
  @media screen and (max-width: 800px) {
    width: 100%;
  }
`;

export const BackgroundImage = styled.div`
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-image: ${({photoURL}) => `url(${photoURL})`};
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