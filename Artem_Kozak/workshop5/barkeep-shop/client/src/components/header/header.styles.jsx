import styled from 'styled-components';
import {Link} from 'react-router-dom';

export const HeaderContainer = styled.div`
  height: 90px;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 20px 60px;
  
  @media screen and (max-width: 800px) {
    display: none;
  }
`;

export const LogoContainer = styled(Link)`
  height: 100%;
  width: 70px;
`;

export const OptionsContainer = styled.div`
  width: 80%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
`;

export const OptionsTextContainer = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
`;

export const OptionLink = styled(Link)`
  padding: 10px 15px;
  cursor: pointer;
`;

export const CurrentUserContainer = styled.div`
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
`;

export const SubMenuContainer = styled.ul`
  display: none;
  border-radius: 5px;
  position: absolute;
  margin: 0;
  padding: 0;
  right: 0;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
`;



export const MenubarItemDropdown = styled(Link)`
  color: black;
  padding: 16px 24px;
  text-decoration: none;
  display: block;
  cursor: pointer; 
  
  &:first-child {
    border-radius: 5px 5px 0 0;
  }
  
  &:last-child {
    border-radius: 0 0 5px 5px;
  }
  
  &:hover {
    background-color: #f1f1f1;
  }
`;

export const MenuItemContainer = styled.div`
  position: relative;
  display: inline-block;
  
  &:hover ${SubMenuContainer} {
    display: block;
  }
`;