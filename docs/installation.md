# Installation Guide
This guide will walk you through the process of setting up the Citizen-Voice project on your local machine. Follow these steps to get the development environment up and running.

The Citizen-Voice project is designed to be set up using Docker Compose, which simplifies the process of managing dependencies and environment configurations. This guide assumes you have basic knowledge of using the command line and Docker.

## Prerequisites
Before you begin, ensure you have the following software installed on your machine:

**Docker** and **Docker Compose**: Docker is required to run the project in isolated containers. Docker Compose is used to manage multi-container Docker applications.

- Install [Docker](https://docs.docker.com/get-started/get-docker/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)


## Getting Started
Follow these steps to set up the Citizen-Voice project:

### Step 1. Clone the Repository

Open a terminal and navigate to the directory where you want to save the project and clone the project repository using the following command:
 ```bash
git clone https://github.com/<your_fork>/Citizen-Voice.git
 ```

### Step 2: Checkout the Development Branch
Navigate into the project directory 
```bash
cd Citizen-Voice
``` 
and switch to the development branch to get the latest updates with 
```bash
git checkout devel
```
### Step 3: Configure Environment Variables
Create a .env file in the project root directory with `nano .env` and paste the following configuration into the .env file and save it:
```
DATABASE=civo
DJANGO_DB_ENGINE=postgis
DB_USER=citizen
DB_PORT=5432
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] djangoapi
```
### Step 4: Set Up Secrets
Create a secrets folder in the root directory:
```bash
mkdir secrets
```
Create a django_token.txt file inside the secrets folder:
```bash
nano secrets/django_token.txt
```
Paste your Django token into this file. For our use case, it is `<django-token-plain-text>`.

Create a postgres_password.txt file inside the secrets folder:
```bash
nano secrets/postgres_password.txt
```
Paste your PostgreSQL superuser password into this file. For our use case, it is ```<postgres-superuser-password>```

### Step 5: Build and Run the Project
Build and run the project using Docker Compose:
```bash
docker compose --env-file .env up --build
```
This command will build the Docker images and start the containers. The web server will be accessible at http://localhost/.
### Verify the Installation
Open a web browser and navigate to http://localhost/ to see the development version of the survey app.

This guide should help you set up the Citizen-Voice project efficiently. If you encounter any issues, please refer to the project's documentation or seek help from the community.


## Front-end
## Back-end
### APIs

## Optional Installation for the Documentation