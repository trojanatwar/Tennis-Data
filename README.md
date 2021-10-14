# To run application from command line

### 1. Install requirements.txt by using following command

For windows

```
    pip install -r requirements.txt
```
For Linux

```
    pip3 install -r requirements.txt
```
### 2. To run web app:

```
    python webapp.py
```
### 3. Open up a browser and type following url
```
    http://127.0.0.1:5000
```

# Run docker image using following commnads 

### 1. Load the docker image name "event_docker.tar" using:

```
    docker load –i event_docker.tar

```

### 2. Check if image is loaded successfully

```
    docker image ls
```

### 3. Now deploy the docker image using:

```
    docker run -it event_docker:latest
```
### 4. Finally check on the browser by following url:

```
    http://127.0.0.1:5000
```


