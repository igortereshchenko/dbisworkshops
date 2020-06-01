import styled from 'styled-components';
import CustomButton from '../custom-button/custom-button.component';

export const CollectionItemContainer = styled.div`
  min-width: 18vw;
  display: flex;
  flex-direction: column;
  align-items: space-between;
  position: relative;

  &:hover {
    .image {
      opacity: 0.8;
    }

    button {
      opacity: 0.85;
      display: flex;
    }
  }
  
  @media screen and (max-width: 1000px) {
    width: 40vw;
    
    &:hover {
      .image {
      opacity: unset;
    }

    button {
      opacity: unset;
    }
  }
}
`;

export const AddButton = styled(CustomButton)`
  width: 80%;
  opacity: 0.7;
  position: absolute;
  top: 255px;
  display: none;
  align-self: center;
  font-size: 14px;
  
  @media screen and (max-width: 1100px) {
    font-size: 10px;
  }  
  
  @media screen and (max-width: 800px) {
    display: block;
    opacity: 0.9;
    min-width: unset;
    padding: 0 10px 0 10px;
  }
  
  @media screen and (max-width: 400px) {
    top: 215px;
  }    
`;

export const BackgroundImage = styled.div`
  width: 100%;
  height: 320px;
  background-size: cover;
  background-position: center;
  margin-bottom: 5px;
  background-image: ${({imageUrl}) => `url(${imageUrl})`};
  
  @media screen and (max-width: 400px) {
    height: 280px;
  } 
`;

export const CollectionFooterContainer = styled.div`
  width: 100%;
  display: flex;
  position: relative;
  justify-content: space-between;
  font-size: 18px;
  
  @media screen and (max-width: 800px) {
    p {
      color: white;
    }
  }
`;

export const NameContainer = styled.p`
  position: relative;
  margin-bottom: 15px;
    
  @media screen and (max-width: 400px) {
    width: unset;
    margin-bottom: 35px;
    font-size: 16px;
  }
`;

export const PriceContainer = styled.p`
  position: relative;
  text-align: right;
    
  @media screen and (max-width: 400px) {
    width: unset;
    margin-bottom: 35px;
  }
`;
