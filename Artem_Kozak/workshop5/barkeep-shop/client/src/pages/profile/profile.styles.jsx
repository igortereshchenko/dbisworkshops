import styled from 'styled-components';

export const ProfilePageContainer = styled.div`
  display: flex;
  font-size: 14px;
  position: relative;
  
  @media screen and (max-width: 800px) {
    flex-direction: column;
    align-items: center;
  }
`;

export const Line = styled.div`
  width: 1 px;
  border-left: 1px solid lightgrey;
  
  @media screen and (max-width: 800px) {
    display: flex;
    align-items: center;
    width: 90%;
    height: 1px;
    border-top: 1px solid lightgrey;
    
    &:last-child {
      display: none;
    }
  }
`;

export const ProfileDataContainer = styled.div`
  width: 700px;
  
  &:first-child {width: 700 px;}
  
  @media screen and (max-width: 800px) {
    width: 100vw;
    
    label, p {
      color: white;
    }
  }
`;