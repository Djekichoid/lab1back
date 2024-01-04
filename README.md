# Lab1

https://lablab1.onrender.com

For running:

```
python3 -m venv env
```
```
source ./env/bin/activate
```
```
pip install flask
```
```
export FLASK_APP=views.py
```
```
docker build --build-arg PORT=<your port> . -t <image_name>:latest
```
```
docker run -it --rm --network=host -e PORT=<your port> <image_name>:latest
```
```
docker-compose build
```
```
docker-compose up
```
