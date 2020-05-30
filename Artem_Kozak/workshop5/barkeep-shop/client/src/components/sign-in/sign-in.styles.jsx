import styled from 'styled-components';

export const SignInContainer = styled.div`
  width: 380px;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    width: 100%;
    margin-bottom: 80px;
  }
`;

export const OrLineContainer = styled.div`
  margin: 35px 0 35px 0;
  width: 100%;
  display: flex;
  flex-direction: line;
  
  hr {
    width: 40%;
    border: none;
    border-bottom: 1px solid grey;
  }
`;


export const SingInAsContainer = styled.div`
  margin-bottom: 18px;
  width: 380px;
  display: flex;
  flex-direction: line;
  
  @media screen and (max-width: 800px) {
    width: 100%;
  }
`;

export const SignInTitle = styled.h2`
  margin: 10px 0;
`;

export const ButtonsBarContainer = styled.div`
  display: flex;
  justify-content: space-between;
`;
