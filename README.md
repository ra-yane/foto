# 2Pack
 
 
## How to dev 2Pack

> Requirements
> * Docker and Docker-compose
> * Python 3 and a Virtual Environment tool (`virtualenv`, `conda`, ...)
> * NodeJS and NPM

### Docker

To run, our project needs some containers :

```
$ docker-compose up -d
```

### Backend

For the Backend, everything is done in Python and we recommend the use of a virtual environment.

```
$ cd back/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then, we just need to adapt the config files for our dev. Copy the `config/config.dev.json` file into `config/config.json`
and modify what is necessary.


### Frontend

For the Frontend, everything is done in Node :

```
$ cd front/
$ npm install
```
