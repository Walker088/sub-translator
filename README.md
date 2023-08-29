# sub-translator

## How to use

```bash
# 1. Python Environment
### Ensure you got python and pipenv installed
### To install pipenv, check out 
### https://pipenv.pypa.io/en/latest/installation/
### Moreover, it's recommmended using pyenv to have
### multiple python in your machine.
### https://github.com/pyenv/pyenv

# 2. Project configuration
### Please check out the config.example.yaml file.
### If you wanna use the google cloud translation api,
### dont forget to create a service account credential
### in your google cloud console, place the credential
### file (in json format) in the project root,
### and specify the path in the config.yaml

$ cp ./config.example.yaml ./config.yaml
$ pipenv shell
# The download process might take a while, use
# "pipenv install --verbose" to see more detailes
$ pipenv install
$ python3 ./main.py
```
