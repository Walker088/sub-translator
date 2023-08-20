# sub-translator

## How to use

```bash
# 1. Python Environment
### Ensure you got python and pipenv installed
### To install pipenv, check out 
### https://pipenv.pypa.io/en/latest/installation/

# 2. Project configuration
### Please check out the config.example.yaml file.
### If you wanna use the google cloud translation api,
### dont forget to create a service account credential
### in your google cloud console, place the credential
### file (in json format) in the project root,
### and specify the path in the config.yaml

$ cp ./config.example.yaml ./config.yaml
$ pipenv shell
$ pipenv install
$ python3 ./main.py
```
