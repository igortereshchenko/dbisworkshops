import styled from 'styled-components';
import {Link} from "react-router-dom";

export const SignUpContainer = styled.div`
  width: 380px;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    width: 100%;
  }
`;

export const SignUpTitle = styled.h2`
  margin: 10px 0;
`;

export const SubDescriptionContainer = styled.h2`
  margin: 10px 0 20px 5px;
  font-size: 10px;
`;

export const TermsLink = styled(Link)`
  color: #497DDD;
  cursor: pointer;
`;
