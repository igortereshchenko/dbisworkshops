import styled from 'styled-components';
import {Link} from 'react-router-dom';

export const HeaderContainer = styled.div`
  height: 50px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  background: black;
  z-index: 5;
  
  @media screen and (min-width: 800px) {
    display: none;
  }
`;

export const LogoContainer = styled(Link)`
  height: 100%;
  padding: 0;
  margin-left: 4vw;
  font-weight: bold;
  color: white;
`;