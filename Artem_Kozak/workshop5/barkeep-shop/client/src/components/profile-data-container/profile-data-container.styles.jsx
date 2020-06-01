import styled from "styled-components";

export const LabelContainer = styled.label`
  padding: 20px;
  color: #505050;
  display: flex;
  width: 35%;
  
  @media screen and (max-width: 800px) {
    padding: 20px 0 20px 0;
    width: 30%;
  }
`;

export const FlexTextsContainer = styled.div`
  display: flex;
  flex-direction: column;
  width: 65%;
  
  @media screen and (max-width: 800px) {
    width: 70%;
  }
`;

export const TextContainer = styled.p`
  margin: 0;
  padding: 10px;
  display: flex;
  width: 100%;
  
  &:first-child {
    padding-top: 20px;
  }
  
  &:last-child {
    padding-bottom: 20px;
  }
`;

export const UserDataContainer = styled.div`
  padding: 0;
  display: flex;
  width: 100%;
`;