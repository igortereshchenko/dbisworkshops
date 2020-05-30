import styled from 'styled-components';

export const HomePageContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const BackgroundMainPageImageContainer = styled.div`
  height: 700px;
  width: 100vw;
  overflow: hidden;
  display: flex;
  // margin-left: -60px;
  margin-right: -60px;
  align-items: center;
  justify-content: center;
  margin: 0 7.5px 15px;
  position: relative;
  
  @media screen and (max-width: 800px) {
    height: 80vh;
  }
`;

export const BackgroundMainPageImage = styled.div`
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: left;
  background-image: url(https://i.ibb.co/4KC5L7h/0119901-12.jpg);
  transition: 3s;
  
  @media screen and (max-width: 800px) {
    background-position: center;
  }
`;


export const ContentMainPageContainer = styled.div`
  text-align: left;
  left: 50px;
  padding: 0 25px;
  display: flex;
  flex-direction: column;
  align-items: left;
  top: 20%;
  justify-content: center;
  position: absolute;
  
  @media screen and (max-width: 800px) {
    justify-content: space-between;
    padding: 10px;
    top: unset;
    left: unset;
    height: 100%;
    width: 100%;
    padding-left: 30px;
  }
  
  @media screen and (max-height: 500px) {
    text-align: left;
    padding: 0 25px;
    align-items: left;
    justify-content: center;
  }
`;
export const TitleBlock = styled.div`
  padding-top: 15px;
  display: flex;
  flex-direction: column;
  
  @media screen and (max-width: 800px) {
    padding-top: 0;
  }
  
  @media screen and (max-height: 500px) {
    &:last-child {
      padding-top: 15px;
    }
  }
`;

export const Title = styled.span`
  font-weight: bold;
  margin-bottom: 6px;
  font-size: 3em;
  color: white;
  margin: 0;
  
  @media screen and (max-width: 800px) {
    font-size: 1.7em;
  }
  
  @media screen and (max-height: 500px) {
    font-size: 1.6em;
  }
`;
