import styled from 'styled-components';

export const TermsOfUseContainer = styled.div`
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    width: 100%;
  }
`;

export const TitleOfArticle = styled.div`
  font-size: 24px;
  margin: 25px 0;
  font-weight: bold;
  
  
`;

export const TitleOfParagraph = styled.div`
  font-size: 16px;
  font-weight: bold;
  margin: 10px 0;
`;

export const TextOfParagraph = styled.div`
  font-size: 14px;
  margin: 10px 0px 30px 0px;
`;

