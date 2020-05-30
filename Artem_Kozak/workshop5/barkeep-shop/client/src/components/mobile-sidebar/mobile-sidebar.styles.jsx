import styled from "styled-components";
import {Link} from "react-router-dom";

export const OptionLink = styled(Link)`
  text-decoration: none;
  color: white;
  opacity: 1;
  font-size: 1.1em;
  font-weight: 400;
  transition: 200ms;
  
  &:hover {
    opacity: 0.5;
    
    p {
      opacity: 0.5;
      transition: 200ms;
    }
  }
`;

export const MenuButtonContainer = styled.div`
  display: flex;
  position: fixed;
  right: 0;
  width: 80px;
  background-color: black;
  z-index: 2;
  border-radius: 0 0 0 40px;
`;

export const Nav = styled.div`
  height: 50px;
  width: 100%;
`;

export const MenuToggle = styled.div`
  display: flex;
  flex-direction: column;
  position: relative;
  top: 15px;
  left: 27px;
  z-index: 3;
  -webkit-user-select: none;
  user-select: none;
`;

export const MenuToggleSpan = styled.span`
  display: flex;
  width: 29px;
  height: 2px;
  margin-bottom: 5px;
  position: relative;
  background: white !important;
  border-radius: 3px;
  z-index: 3;
  transform-origin: 5px 0;
  transition: transform 0.5s cubic-bezier(0.77, 0.2, 0.05, 1.0),
  background 0.5s cubic-bezier(0.77, 0.2, 0.05, 1.0),
  opacity 0.55s ease;
  
  &:first-child {
    transform-origin: 0 0;
  }
  
  &:nth-last-child(2) {
    transform-origin: 0 100%;
  }
`;

export const MenuItem = styled.ul`
  list-style-type: none;
  position: fixed;
  width: 100vw;
  height: 120vh;
  margin: -50px 0 0 -50vw;
  padding: 15vh 30px 50px;
  background-color: black;
  -webkit-font-smoothing: antialiased;
  transform-origin: 0 0;
  transform: translate(100%, 0);
  transition: transform 0.5s cubic-bezier(0.77, 0.2, 0.05, 1.0);
  z-index: 2;
  
  & .userExit {
    position: absolute;
    top: 85vh;
  }
`;

export const FullScreenMenuContainer = styled.div`
  display: fixed;
  opacity: 0;
  overflow: hidden;
  height: 110vh;
  width: 110vw;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  margin: 0;
  padding: 0;
`;

export const CheckoutInput = styled.input`
  display: flex;
  width: 40px;
  height: 40px;
  position: absolute;
  top: -15px;
  left: -8px;
  cursor: pointer;
  opacity: 0;
  z-index: 4;
  
  &:checked ~ span {
    opacity: 1;
    transform: rotate(45deg) translate(-3px, -1px);
  }
  
  &:checked ~ span:nth-last-child(3) {
    opacity: 0;
    transform: rotate(0deg) scale(0.2, 0.2);
  }
  
  &:checked ~ span:nth-last-child(2) {
    transform: rotate(-45deg) translate(0, -1px);
  }
  
  &:checked ~ ul {
    transform: none;
  }
    
  &:checked ~ ${FullScreenMenuContainer} {
    display: unset;
  }
  
`;


export const ListItem = styled.li`
  padding: 10px 0;
  transition-delay: 2s;
  
  div {
    cursor: pointer;
  }
`;
