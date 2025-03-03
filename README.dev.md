# Developer documentation

If you're looking for user documentation, go [here](README.md).

## API Docker container

The api can be reproduced using docker compose as follows:

1. Clone the repository, the latest version is in the `devel` branch.
2. Add a `.env` file to the root of the repository with the following variables.

```shell
DATABASE=civo
JDANGO_DB_ENGINE=postgis
DB_USER=citizen
DB_PORT=5432
DJANGO_DEBUG=1  
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

3. Create a directory in the root of the repository called `secrets/`, and create the secrets for the Django token and the database password as follows:

```shell
# file name: django_token.txt
<django-token-plain-text>
```

```shell
# file name: postgres_password.txt
<postgres-superuser-password>
```

4. Build and run using docker compose. The webserver will run on port 80 at `localhost`. The database will be populated with sample data.

```shell
docker compose --env-file .env up --build
```

5. Go to the Survey API root: http://localhost/api/v2/

**Open API**
- A schema of the API can be downloaded from: http://localhost/api/v2/schema
- Auto generated documentation is available at: http://localhost/api/v2/schema/redoc

### Civilian API

An API for the dasboard can be accessed at: http://localhost/civilian/v1/
With the corresponding schemas and documentation at:
- Schema: http://localhost/civilian/v1/schema
- Documentation: http://localhost/civilian/v1/schema/redoc

The 'answers' endpoint provides the list of answers for questions that contain spatial geometries. 
One can navigate long list of answers by using the `page` parameter. The `topics` keyword in `question` contains the name of the categories for the legend in the dashboard. The `geojson` keyword in `mapview` contains valid GeoJson for all the geometries related to an answer. Notice, that the *property* `annotation` of each geometry contains a text, which if not a empty string,  shall be display as a pop-up on geometries in the dashboard. 

Coordinates of the geometries are the WSG84 reference system.

Answers can be filtered by survey, question or both as follows:
- By survey: `http://localhost/civilian/v1/answers/?survey=3`
- By question: `http://localhost/civilian/v1/answers/?question=6`
- By survey and question: `http://localhost/civilian/v1/answers/?survey=3&question=6`

Response example:

```json

{
    "count": 12,
    "next": "http://localhost:8000/civilian/v1/answers/?page=2",
    "previous": null,
    "results": [
        {
            "id": 125,
            "created": "2024-12-09T09:54:56.249000Z",
            "body": "",
            "question": {
                "text": "In your neighbourhood, where would you like to see more green areas, and what kind of green would you like to see there (flowers, trees, vegetables)?",
                "topics": [
                    "Lack of green"
                ]
            },
            "mapview": {
                "location": {
                    "geojson": {
                        "type": "FeatureCollection",
                        "features": [
                            {
                                "id": 185,
                                "type": "Feature",
                                "geometry": {
                                    "type": "Point",
                                    "coordinates": [
                                        4.36757,
                                        52.006762
                                    ]
                                },
                                "properties": {
                                    "annotation": "trees"
                                }
                            },
                            {
                                "id": 186,
                                "type": "Feature",
                                "geometry": {
                                    "type": "Point",
                                    "coordinates": [
                                        4.366964,
                                        52.007716
                                    ]
                                },
                                "properties": {
                                    "annotation": "flowers"
                                }
                            }
                        ]
                    }
                }
            }
        },
        ...
    ]
}
```

## Development installation

Follow the instruction below to set up a development environment. We use Python 3.10 and Django 4.0.x for development.

### Requirements

* [GDAL 3.3.2](https://gdal.org/download.html) or later
* [PostgreSQL](https://www.postgresql.org/) database with the [PostGIS](https://postgis.net/install/) extension

### Create a virtual environment

Create a virtual environment, activate it, and install the development dependencies in it. This will enable you to run the tests and web-apps later.
[For Windows read here.](https://medium.com/co-learning-lounge/create-virtual-environment-python-windows-2021-d947c3a3ca78)

```shell
# Create a virtual environment, e.g. with
python3 -m venv ./venv

# activate virtual environment
source venv/bin/activate

# make sure to have a recent version of pip and setuptools
python3 -m pip install --upgrade pip setuptools

# (from the project root directory)
# install development dependencies
pip install -r requirements.txt
```

## Running the Django App

1. Create a `local.env` file with a secret key for the django project, and the database configuration, such as:
    
    ```shell
    # local.env file root directory

    POSTGRES_DBASE=citizen
    JDANGO_DB_ENGINE=postgis
    DATABASE_ENGINE=postgis
    POSTGRES_USER=citizen
    DB_PORT=5432
    DJANGO_DEBUG=1  # run in debug mode
    DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
    DB_HOST=localhost # Comment for docker
    SECRET_KEY=django-insecure-#(7^@z1!1 
    POSTGRES_PWD='admin@voice'
    TEST_DBASE=''
    ```

2. Uncomment the line to load `local.env` in `citizenvoice/citizenvoice/settings.py`:

```python
# load_dotenv("../local.env")
```
    
3. Run the development server from `citizenvoice/` directory. Saved changes will be automatically reloaded:

    ```shell
    python manage.py runserver
    ```

## Running the tests

Running the tests requires an activated virtual environment with the development tools installed.

```shell
# unit tests
cd ./citizenvoice
python manage.py test
```

## Making a release

<Instructions to make a release.>

### Preparation

1. Make sure the `CHANGELOG.md` has been updated
2. Verify that the information in `CITATION.cff` is correct, and that `.zenodo.json` contains equivalent data
3. Make sure that `version` in [setup.cfg](setup.cfg) and  `version` in [CITATION.cff](CITATION.cff) have been bumped to the to-be-released version of the template
4. Run the unit tests with `python manage.py test`
5. Go through the steps outlined above for [generating a new package from the command line](#), and verify that the generated package works as it should.

### GitHub

1. Make sure that the GitHub-Zenodo integration is enabled for https://github.com/NLeSC/python-template
1. Go to https://github.com/NLeSC/python-template/releases and click `Draft a new release`
