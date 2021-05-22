# flaskBlog
## Introduction
This is my homework for database class.  
Maybe I will continue to study Flask in future.

## Install
If you want to run this app, you need have **Python 3.8** (or newer) and [Poetry](https://python-poetry.org/)

After installed above of these application, clone this repo and run command in the folder :
```shell
poetry install
```

it'll create a new virtualenv, you can run this virtualenv, just run these command:
```shell
poetry shell
flask run
```

And you can try to explore `http://127.0.0.1:5000`, you can see the newest devlopment progress.

## Enable Debug Mode

Something can show only Debug mode is opened, create `.env` in the folder and type this:
```text
FLASK_DEBUG=1
```
Run `flask run` and you can see what you want.