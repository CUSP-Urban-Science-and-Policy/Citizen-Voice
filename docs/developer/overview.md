# Application Overview

The Citizen Voice ecosystem is designed to facilitate community engagement through various tools and platforms. It consists of several componets that work together to allow users to create, answer, and visualize questionnaires.

## Components

### Citizen Mapping

A front-end application that enables users to create and answer questionnaires (surveys). The application is built using Nuxt.js and interacts with the Citizen Voice APIs to manage questionnaire data.

### Community Dashboard
A front-end application that allows users to visualize answers to questionnaires. The application is built using Nuxt.js and interacts with the Civilian API to fetch and display data (answerrs to questions) on a map. Only geographic questions are displayed on the map. Users can filter data based on topics associated with each question. 

### Application Programming Interfaces

The system provides two APIs that interact with the Citizen Mapping tool and the Communicty Dashboard. APIs are implemented using Django REST Framework, and follow the OpenAPI specification for documentation. 

- **Voice API**: This API is used by the Citizen Mapping tool to manage questionnaire data, including creating, updating, and retrieving questionnaires (surveys) and their answers.
- **Civilian API**: This API is used by the Community Dashboard to fetch and display answers on a map. It allows applications to retrieve the topics associated with a questionnaire and filter answers based on survey ID.

### Code Organization

The [codebase](https://github.com/CUSP-Urban-Science-and-Policy/Citizen-Voice) is organized into several directories, each serving a specific purpose:

```shell
.
├── maptool
│   ├── yarn.lock
│   ├── utils
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── stores
│   ├── run
│   ├── public
│   ├── plugins
│   ├── pages
│   ├── package.json
│   ├── openapi
│   ├── nuxt.config.js
│   ├── node_modules
│   ├── middleware
│   ├── layouts
│   ├── constants
│   ├── components
│   ├── assets
│   ├── app.vue
│   ├── README.md
│   └── Dockerfile
├── cv-portal
│   ├── yarn.lock
│   ├── tsconfig.json
│   ├── server
│   ├── run
│   ├── public
│   ├── pages
│   ├── package.json
│   ├── nuxt.config.ts
│   ├── node_modules
│   ├── layouts
│   ├── eslint.config.mjs
│   ├── components
│   ├── assets
│   ├── app.vue
│   ├── README.md
│   └── Dockerfile
├── citizenvoice
│   ├── voice
│   ├── users
│   ├── tests
│   ├── survey_design
│   ├── respondent
│   ├── requirements.txt
│   ├── openapi.yml
│   ├── media
│   ├── manage.py
│   ├── civilian-db.json
│   ├── civilian
│   ├── citizenvoice
│   ├── authentication
│   └── Dockerfile
├── WAIVER
├── README.md
├── README.dev.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CITATION.cff
└── CHANGELOG.md

```

The `maptool` directory contains the source code for the Citizen Mapping application, while the `cv-portal` directory contains the source code for the Community Dashboard. The `citizenvoice` directory contains the Django application that implements the Voice and Civilian APIs.


### Containerization
The entire system is containerized using Docker, allowing for easy deployment and management of the different components. In its containerized form, the system consists of five services:

- **postgis_db**: A PostgreSQL database with PostGIS extension for geographic data storage. A quirement for the Voice and Civilian APIs. 
- **api**: The Django application that implements the Voice and Civilian APIs.
- **maptool**: The Citizen Mapping application, which allows users to create and answer questionnaires.
- **cvportal**: The Community Dashboard application, which allows users to visualize answers on a map.
- **nginx**: A reverse proxy server that routes requests to the appropriate service.

