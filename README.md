## Python Flask Website

This repo contains code for my personal blog related to tech and professional interests. It is implemented using python's Flask framework.

## COMMANDS USED

### Azure

````
```
az login
az group create --name flask-blog --location eastus
az group list
az account list
az account set -s sandbox sub
az account show
az acr login --name containers38472
```
````

### Docker

````
```
docker build -t myimage .
docker images
docker images -a
**<name>:<name> intermediate images used to build other images
docker image rm python:latest
docker rm -f serene_allen - this removes container
docker container ls (--all)
docker container rm -f $(docker ps -aq)
docker ps - confirm running containers
docker run -t -i python:3.6-alpine - enter @ interpreter


```
````
