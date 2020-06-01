import {createGlobalStyle} from "styled-components";

export const GlobalStyle = createGlobalStyle`
    body {
        font-family: 'Comfortaa', sans-serif;
        padding: 0;
        z-index: 0;
        
        @media screen and (max-width: 800px) {
            padding: 0;
            background-color: #121212;
            
            a, h1, h2, span, label {
              color: white;
            }
        }
    }
    
    a {
        text-decoration: none;
        color: black;
    }
    
    * {
        box-sizing: border-box;
    }
`;