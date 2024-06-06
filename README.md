# Library system - API Gateway


## General info
This app is an API gateway which is part of library system microservices composed of the following:
<ul>
<li>Library (building in progress...)</li>
<li>Forum (building in progress...)</li>
</ul>

## Tech-stack
<ul>
<li>Python</li>
<li>FastAPI</li>
<li>Auth0</li>
<li>Docker Compose</li>
</ul>

## Setup

To run this project on your machine it is required to have installed previously Docker Compose on your computer. For further information, see [documentation](https://docs.docker.com/compose/install/ "Install docker").


1. [*Clone*](https://help.github.com/articles/cloning-a-repository/) the repository on your machine.
2. Create a .env file in deployment/prod/ folder, in which you'll have to set the variables below. Please note that this app is using Auth0 for authentication, so Auth0 account is required.
       <details>
       <summary>see .env file variables</summary>
        AUTH0_DOMAIN<br>
        AUTH0_API_AUDIENCE<br>
        AUTH0_ISSUER<br>
        AUTH0_ALGORITHMS<br>
        LIBRARY_ENDPOINT<br>
        FORUM_ENDPOINT<br>
        </details>
3. In deployment/prod/ folder run the command in a terminal: `docker compose up -d`.
4. Once the app has started, open [localhost](http://localhost/) in a web browser.
