import styled from 'styled-components';
import {css} from "styled-components";

const textColor = css`
  color: #3d7ee5;
`;

export const ProfileAddDataButtonContainer = styled.div`
  display: flex;
  flex-direction: row;
`;

export const AddButton = styled.button`
  border: none;
  background: none;
  font-family: 'Comfortaa', sans-serif;
  font-size: 14px;
  padding: 0;
  margin: 0;
  cursor: pointer;
  display: flex;
  justify-content: center;
  ${textColor}
  
  span {
    padding-top: 1px;
    height: 18px;
    font-size: 16px;
    margin-right: 3px;
  }
  
  &: hover {
    color: #1752af;
    transition: color .4s ease 0s;
  }
`;
