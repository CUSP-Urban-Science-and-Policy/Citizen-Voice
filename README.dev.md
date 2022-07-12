# Developer documentation

If you're looking for user documentation, go [here](README.md).

## Development installation

Follow the instruction below to set up a development environment. We use Python 3.10 and Django 4.0.x for development.

### Create a virtual environment

Make a virtual environment, activate it, and install the development dependencies in it. This will enable you to run the tests and web-apps later.
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

1. Create a `.env` file with a secret key for the django project, such as:
    
    ```shell
    # .env file in ./citizenvoice/
    SECRET_KEY = 'django-insecure-<a hexadecimal string>'
    ```
1. Run the development server from the project directory. Saved changes will be authomatically reloaded:

    ```shell
    python manage.py runserver
    ```

## Running the tests

Running the tests requires an activated virtual environment with the development tools installed.

```shell
# unit tests
pytest
pytest tests/
```


## Making a release

### Preparation

1. Make sure the `CHANGELOG.md` has been updated
2. Verify that the information in `CITATION.cff` is correct, and that `.zenodo.json` contains equivalent data
3. Make sure that `version` in [setup.cfg](setup.cfg) and  `version` in [CITATION.cff](CITATION.cff) have been bumped to the to-be-released version of the template
4. Run the unit tests with `XXX`
5. Go through the steps outlined above for [generating a new package from the command line](#), and verify that the generated package works as it should.

### GitHub

1. Make sure that the GitHub-Zenodo integration is enabled for https://github.com/NLeSC/python-template
1. Go to https://github.com/NLeSC/python-template/releases and click `Draft a new release`