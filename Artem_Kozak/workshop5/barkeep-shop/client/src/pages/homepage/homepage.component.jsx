import React from 'react';

import Directory from '../../components/directory/directory.component';

import {
    BackgroundMainPageImage,
    BackgroundMainPageImageContainer,
    ContentMainPageContainer,
    HomePageContainer,
    TitleBlock,
    Title
} from './homepage.styles';

const HomePage = () => (
    <HomePageContainer>
        <BackgroundMainPageImageContainer>
            <BackgroundMainPageImage className={"background-image"}/>
            <ContentMainPageContainer>
                <TitleBlock>
                    <Title>Только лучшее</Title>
                    <Title>для бара</Title>
                </TitleBlock>
                <TitleBlock>
                    <Title>Теперь доступно</Title>
                    <Title>каждому</Title>
                </TitleBlock>
            </ContentMainPageContainer>
        </BackgroundMainPageImageContainer>
        <Directory/>
    </HomePageContainer>
);

export default HomePage;
